"""
BlackRose Mini App Backend
FastAPI API для Telegram Mini App
"""

import re
import sys
from functools import lru_cache
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse

# Добавляем корень проекта в sys.path для импорта гайдов
sys.path.append(str(Path(__file__).parent.parent.parent))

# Импортируем данные из существующего файла
from guides import CONTENT, MAIN_CATEGORIES, SUBMENUS

# Инициализация приложения
app = FastAPI(
    title="BlackRose Mini App API",
    description="API для Telegram Mini App - справочник гильдии",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS middleware для Telegram WebApp
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Простой счётчик просмотров (в памяти)
guide_stats: dict[str, int] = {}


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================


def _extract_emoji(text: str) -> str:
    """Извлекает первый эмодзи из текста для использования как иконка"""
    emoji_pattern = re.compile(
        "["
        "\U0001f600-\U0001f64f"  # emoticons
        "\U0001f300-\U0001f5ff"  # symbols & pictographs
        "\U0001f680-\U0001f6ff"  # transport & map symbols
        "\U0001f1e0-\U0001f1ff"  # flags
        "\U00002702-\U000027b0"
        "\U000024c2-\U0001f251"
        "]+",
        flags=re.UNICODE,
    )
    match = emoji_pattern.search(text)
    return match.group(0) if match else "📄"


# =============================================================================
# HEALTH CHECK & INFO
# =============================================================================


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "ok",
        "service": "BlackRose Mini App API",
        "version": "1.0.0",
        "endpoints": [
            "/api/categories",
            "/api/category/{key}",
            "/api/guide/{key}",
            "/api/search",
            "/api/stats",
        ],
    }


@app.get("/api/info")
async def get_info():
    """Общая информация о приложении"""
    total_photos = sum(
        (
            len(guide.get("photo", []) or [])
            if isinstance(guide.get("photo"), list)
            else (1 if guide.get("photo") else 0)
        )
        for guide in CONTENT.values()
    )
    return {
        "total_categories": len(MAIN_CATEGORIES),
        "total_guides": len(CONTENT),
        "total_photos": total_photos,
        "categories": list(MAIN_CATEGORIES.keys()),
    }


# =============================================================================
# CATEGORIES ENDPOINTS
# =============================================================================


@app.get("/api/categories")
@lru_cache(maxsize=1)
def get_categories():
    """Получить список всех категорий"""
    categories = []
    for key, data in MAIN_CATEGORIES.items():
        # Поддержка старого формата (строка) и нового (dict)
        if isinstance(data, dict):
            title = data.get("title", key)
            icon = data.get("icon")
        else:
            title = data
            icon = None

        categories.append(
            {"key": key, "title": title, "icon": icon, "count": len(SUBMENUS.get(key, []))}
        )

    return {"categories": categories}


@app.get("/api/category/{category_key}")
async def get_category(category_key: str):
    """Получить список гайдов в категории"""
    if category_key not in SUBMENUS:
        raise HTTPException(
            status_code=404,
            detail=f"Category '{category_key}' not found. Available: {list(SUBMENUS.keys())}",
        )

    items = []
    for item in SUBMENUS[category_key]:
        # Поддержка старого формата (tuple из 2 элементов) и нового (3 элемента)
        if len(item) == 3:
            key, title, icon = item
        else:
            key, title = item
            icon = None

        guide = CONTENT.get(key, {})

        # Проверяем media
        photo = guide.get("photo")
        has_photo = (
            bool(photo) if isinstance(photo, (list, str)) and photo not in [None, "None"] else False
        )

        video = guide.get("video")
        has_video = (
            bool(video) if isinstance(video, (list, str)) and video not in [None, "None"] else False
        )

        items.append(
            {
                "key": key,
                "title": title,
                "icon": icon,
                "preview": guide.get("text", "")[:150].strip() + "...",
                "has_photo": has_photo,
                "has_video": has_video,
                "views": guide_stats.get(key, 0),
            }
        )

    # Получаем title категории
    category_data = MAIN_CATEGORIES.get(category_key, {})
    if isinstance(category_data, dict):
        category_title = category_data.get("title", category_key)
    else:
        category_title = category_data

    return {
        "category": {"key": category_key, "title": category_title},
        "items": items,
        "total": len(items),
    }


# =============================================================================
# GUIDE ENDPOINTS
# =============================================================================


@lru_cache(maxsize=50)
def _get_guide_content(guide_key: str) -> dict | None:
    """Кэшированная функция получения контента гайда"""
    return CONTENT.get(guide_key)


@app.get("/api/guide/{guide_key}")
async def get_guide(guide_key: str):
    """Получить полный контент гайда"""
    # Считаем просмотр
    guide_stats[guide_key] = guide_stats.get(guide_key, 0) + 1

    # Получаем кэшированный контент
    guide = _get_guide_content(guide_key)

    if not guide:
        similar = [k for k in CONTENT.keys() if guide_key.lower() in k.lower()]
        raise HTTPException(
            status_code=404,
            detail={
                "message": f"Guide '{guide_key}' not found",
                "similar": similar[:5] if similar else None,
                "available_guides": list(CONTENT.keys())[:10],
            },
        )

    # Обработка photo
    photo = guide.get("photo")
    photo_list = []
    if photo:
        if isinstance(photo, list):
            photo_list = [p for p in photo if p and p != "None"]
        elif isinstance(photo, str) and photo not in ["None", ""]:
            photo_list = [photo]

    # Обработка video
    video = guide.get("video")
    video_list = []
    if video:
        if isinstance(video, list):
            video_list = [v for v in video if v and v != "None"]
        elif isinstance(video, str) and video not in ["None", ""]:
            video_list = [video]

    # Обработка document
    document = guide.get("document")
    doc_list = []
    if document:
        if isinstance(document, list):
            doc_list = [d for d in document if d and d != "None"]
        elif isinstance(document, str) and document not in ["None", ""]:
            doc_list = [document]

    # Иконка гайда
    title = guide.get("title", guide_key)
    icon = guide.get("icon")

    return {
        "key": guide_key,
        "title": title,
        "icon": icon,
        "text": guide.get("text", ""),
        "photo": photo_list,
        "video": video_list,
        "document": doc_list,
        "views": guide_stats[guide_key],
        "media_count": len(photo_list) + len(video_list) + len(doc_list),
    }


# =============================================================================
# SEARCH ENDPOINT
# =============================================================================


@app.get("/api/search")
async def search_guides(
    q: str = Query(..., min_length=2, description="Поисковый запрос"),
    limit: int = Query(10, ge=1, le=50, description="Максимум результатов"),
):
    """Поиск по гайдам"""
    query = q.lower().strip()
    results = []

    for key, guide in CONTENT.items():
        text = guide.get("text", "").lower()

        if query in key.lower() or query in text:
            relevance = 0
            if query in key.lower():
                relevance += 10
            relevance += text.count(query)

            results.append(
                {
                    "key": key,
                    "title": guide.get("title", key),
                    "icon": guide.get("icon"),
                    "preview": guide.get("text", "")[:200].strip() + "...",
                    "relevance": relevance,
                    "views": guide_stats.get(key, 0),
                    "has_media": bool(guide.get("photo") or guide.get("video")),
                }
            )

    results.sort(key=lambda x: x["relevance"], reverse=True)

    return {"query": q, "total_found": len(results), "results": results[:limit]}


# =============================================================================
# STATS ENDPOINT
# =============================================================================


@app.get("/api/stats")
async def get_stats():
    """Статистика использования"""
    total_views = sum(guide_stats.values())

    top_guides = sorted(guide_stats.items(), key=lambda x: x[1], reverse=True)[:10]

    return {
        "total_views": total_views,
        "unique_guides_viewed": len(guide_stats),
        "top_guides": [{"key": key, "views": views} for key, views in top_guides],
        "cache_info": _get_guide_content.cache_info(),
    }


# =============================================================================
# SERVE FRONTEND
# =============================================================================

frontend_dir = Path(__file__).parent.parent / "frontend"


@app.get("/frontend")
async def serve_index():
    """Отдаёт index.html"""
    index_path = frontend_dir / "index.html"
    if not index_path.exists():
        return {"error": "index.html not found", "frontend_dir": str(frontend_dir)}
    return FileResponse(index_path)


# =============================================================================
# ERROR HANDLERS
# =============================================================================


@app.exception_handler(404)
async def not_found_handler(request, exc):
    return JSONResponse(status_code=404, content={"error": "Not found", "path": str(request.url)})


@app.exception_handler(Exception)
async def general_error_handler(request, exc):
    return JSONResponse(
        status_code=500, content={"error": "Internal server error", "detail": str(exc)}
    )


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, log_level="info")
