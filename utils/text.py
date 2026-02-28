from config import TEXT_SPLIT_LIMIT


def split_text(text: str, limit: int = None) -> list[str]:
    """Разбивает текст на части по limit символов"""
    if limit is None:
        limit = TEXT_SPLIT_LIMIT
    
    chunks = []
    while len(text) > limit:
        split_index = text.rfind(' ', 0, limit)
        if split_index == -1:
            split_index = limit
        chunks.append(text[:split_index])
        text = text[split_index:].lstrip()
    if text:
        chunks.append(text)
    return chunks