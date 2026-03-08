"""
BlackRose Mini App - Управление иконками
Организованы по 4 категориям для удобного использования
"""

# ═══════════════════════════════════════════════════════
# 📁 БАЗОВЫЙ URL ДЛЯ ИЗОБРАЖЕНИЙ
# ═══════════════════════════════════════════════════════
BASE_URL = "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons"

# ═══════════════════════════════════════════════════════
# 🎓 CLASS_ETC (Классы, мечи, реликвии и прочее)
# ═══════════════════════════════════════════════════════
CLASS_ETC = {
    # Классы
    "class_s": f"{BASE_URL}/class_etc/class_s.png",
    "class_c": f"{BASE_URL}/class_etc/class_c.png",
    "class_b": f"{BASE_URL}/class_etc/class_b.png",
    "class_a": f"{BASE_URL}/class_etc/class_a.png",
    "class_terra": f"{BASE_URL}/class_etc/class_terra.png",
    "class_nova": f"{BASE_URL}/class_etc/class_nova.png",
    "class_sid": f"{BASE_URL}/class_etc/class_sid.png",
    "class_last": f"{BASE_URL}/class_etc/class_last.png",
    
    # Мечи
    "sword_m1": f"{BASE_URL}/class_etc/sword_m1.png",
    "sword_opp": f"{BASE_URL}/class_etc/sword_opp.png",
    "sword_orb": f"{BASE_URL}/class_etc/sword_orb.png",
    "sword_ancient": f"{BASE_URL}/class_etc/sword_ancient.png",
    "sword_eternal": f"{BASE_URL}/class_etc/sword_eternal.png",
    "sword_dream": f"{BASE_URL}/class_etc/sword_dream.png",
    
    # Реликвии
    "relic_weapon": f"{BASE_URL}/class_etc/relic_weapon.png",
    "relic_armor": f"{BASE_URL}/class_etc/relic_armor.png",
    "relic_accessory": f"{BASE_URL}/class_etc/relic_accessory.png",
    
    # Другое
    "stage": f"{BASE_URL}/class_etc/stage.png",
    "ds": f"{BASE_URL}/class_etc/ds.png",
    "attack": f"{BASE_URL}/class_etc/attack.png",
    "crit_damage": f"{BASE_URL}/class_etc/crit_damage.png",
    "hp": f"{BASE_URL}/class_etc/hp.png",
    "rxp": f"{BASE_URL}/class_etc/rxp.png",
    "check": f"{BASE_URL}/class_etc/check.png",
    "cross": f"{BASE_URL}/class_etc/cross.png",
    "warning": f"{BASE_URL}/class_etc/warning.png",
    "info": f"{BASE_URL}/class_etc/info.png",
    "star": f"{BASE_URL}/class_etc/star.png",
    "diamond": f"{BASE_URL}/class_etc/diamond.png",
    "gold": f"{BASE_URL}/class_etc/gold.png",
    "gem": f"{BASE_URL}/class_etc/gem.png",
}

# ═══════════════════════════════════════════════════════
# ⚔️ PROMOTION (Промоуты)
# ═══════════════════════════════════════════════════════
PROMOTION = {
    # Иконки промоутов
    "promo_ether": f"{BASE_URL}/promotion/Ether.png",
    "promo_black_mithril": f"{BASE_URL}/promotion/Black Mythril.png",
    "promo_demonite": f"{BASE_URL}/promotion/Demon Metal.png",
    "promo_dragonos": f"{BASE_URL}/promotion/Dragonos.png",
    "promo_blood": f"{BASE_URL}/promotion/Ragnablood.png",
    "promo_frost": f"{BASE_URL}/promotion/Warfrost.png",
    "promo_nox": f"{BASE_URL}/promotion/Dark Nox.png",
    "promo_abyss": f"{BASE_URL}/promotion/Blue Abyss.png",
    "promo_infinat": f"{BASE_URL}/promotion/Infinaut.png",
    "promo_cyclone": f"{BASE_URL}/promotion/Cyclos.png",
    "promo_ancient": f"{BASE_URL}/promotion/Ancient Canine.png",
    "promo_gigalor": f"{BASE_URL}/promotion/Gigarock.png",
    
    # Иконка категории промоутов
    "cat_promoutes": f"{BASE_URL}/promotion/cat_promoutes.png",
}

# ═══════════════════════════════════════════════════════
# ⚡ SKILLS (Навыки и камни)
# ═══════════════════════════════════════════════════════
SKILLS = {
    # Камни навыков
    "skill_water": f"{BASE_URL}/skills/skill_water.png",
    "skill_earth": f"{BASE_URL}/skills/skill_earth.png",
    "skill_wind": f"{BASE_URL}/skills/skill_wind.png",
    "skill_fire": f"{BASE_URL}/skills/skill_fire.png",
    
    # Навыки
    "skill_meditation": f"{BASE_URL}/skills/skill_meditation.png",
    "skill_hell_strike": f"{BASE_URL}/skills/skill_hell_strike.png",
    "skill_rage": f"{BASE_URL}/skills/skill_rage.png",
    "skill_elf_song": f"{BASE_URL}/skills/skill_elf_song.png",
    "skill_war_wisdom": f"{BASE_URL}/skills/skill_war_wisdom.png",
    
    # Элементы
    "element_fire": f"{BASE_URL}/skills/element_fire.png",
    "element_earth": f"{BASE_URL}/skills/element_earth.png",
    "element_wind": f"{BASE_URL}/skills/element_wind.png",
    "element_water": f"{BASE_URL}/skills/element_water.png",
}

# ═══════════════════════════════════════════════════════
# 👻 SPIRIT (Духи и фамильяры) - ИСПРАВЛЕНО!
# ═══════════════════════════════════════════════════════
SPIRIT = {  # Было SPIRIT_FAMILIARS
    # Духи (Spirits)
    "spirit_noah": f"{BASE_URL}/spirit/spirit_noah.png",
    "spirit_loar": f"{BASE_URL}/spirit/spirit_loar.png",
    "spirit_sala": f"{BASE_URL}/spirit/spirit_sala.png",
    "spirit_mum": f"{BASE_URL}/spirit/spirit_mum.png",
    "spirit_bo": f"{BASE_URL}/spirit/spirit_bo.png",
    "spirit_radon": f"{BASE_URL}/spirit/spirit_radon.png",
    "spirit_zappy": f"{BASE_URL}/spirit/spirit_zappy.png",
    "spirit_kart": f"{BASE_URL}/spirit/spirit_kart.png",
    "spirit_herh": f"{BASE_URL}/spirit/spirit_herh.png",
    "spirit_todd": f"{BASE_URL}/spirit/spirit_todd.png",
    "spirit_luga": f"{BASE_URL}/spirit/spirit_luga.png",
    "spirit_ark": f"{BASE_URL}/spirit/spirit_ark.png",
    "spirit_nerh": f"{BASE_URL}/spirit/spirit_nerh.png",
    "spirit_boo": f"{BASE_URL}/spirit/spirit_boo.png",
    
    # Фамильяры
    "familiar_hikuna": f"{BASE_URL}/spirit/familiar_hikuna.png",
    "familiar_hikurion": f"{BASE_URL}/spirit/familiar_hikurion.png",
    "familiar_tikuna": f"{BASE_URL}/spirit/familiar_tikuna.png",
    "familiar_a": f"{BASE_URL}/spirit/familiar_a.png",
    
    # Звёзды и уровни
    "star_1": f"{BASE_URL}/spirit/star_1.png",
    "star_3": f"{BASE_URL}/spirit/star_3.png",
    "star_5": f"{BASE_URL}/spirit/star_5.png",
    "star_6": f"{BASE_URL}/spirit/star_6.png",
    "star_7": f"{BASE_URL}/spirit/star_7.png",
    "star_8": f"{BASE_URL}/spirit/star_8.png",
    "awaken_e": f"{BASE_URL}/spirit/awaken_e.png",
    "awaken_a": f"{BASE_URL}/spirit/awaken_a.png",
}

# ═══════════════════════════════════════════════════════
# 📂 КАТЕГОРИИ ИНФОРМАЦИИ
# ═══════════════════════════════════════════════════════
INFO_CATEGORIES = {
    "info_general": f"{BASE_URL}/info_general.png",
    "info_event": f"{BASE_URL}/info_event.png",
    "info_rage": f"{BASE_URL}/info_rage.png",
    "info_ads": f"{BASE_URL}/info_ads.png",
    "info_pets": f"{BASE_URL}/info_pets.png",
    "info_sword": f"{BASE_URL}/info_sword.png",
    "info_farm": f"{BASE_URL}/info_farm.png",
    "info_spirit": f"{BASE_URL}/info_spirit.png",
    "info_build": f"{BASE_URL}/info_build.png",
}

# ═══════════════════════════════════════════════════════
# 🌳 ПРИКЛЮЧЕНИЯ
# ═══════════════════════════════════════════════════════
ADVENTURES = {
    "adv_adventures": f"{BASE_URL}/adv_adventures.png",
    "adv_cave": f"{BASE_URL}/adv_cave.png",
    "adv_rift": f"{BASE_URL}/adv_rift.png",
    "adv_shelter": f"{BASE_URL}/adv_shelter.png",
    "adv_mind": f"{BASE_URL}/adv_mind.png",
    "adv_forest": f"{BASE_URL}/adv_forest.png",
}

# ═══════════════════════════════════════════════════════
# 🛡 ГИЛЬДИЯ
# ═══════════════════════════════════════════════════════
GUILD = {
    "guild_guild": f"{BASE_URL}/guild_guild.png",
    "guild_wyvern": f"{BASE_URL}/guild_wyvern.png",
    "guild_cooking": f"{BASE_URL}/guild_cooking.png",
}

# ═══════════════════════════════════════════════════════
# 📦 ВСЕ ИКОНКИ (объединённый словарь)
# ═══════════════════════════════════════════════════════
ALL_ICONS = {
    **CLASS_ETC,
    **PROMOTION,
    **SKILLS,
    **SPIRIT,  # Было SPIRIT_FAMILIARS
    **INFO_CATEGORIES,
    **ADVENTURES,
    **GUILD,
}


# ═══════════════════════════════════════════════════════
# 🔧 HELPER ФУНКЦИИ
# ═══════════════════════════════════════════════════════

def get_icon(name: str, default: str = None) -> str:
    """
    Получить URL иконки по имени
    
    Args:
        name: Имя иконки
        default: Значение по умолчанию если не найдена
    
    Returns:
        URL иконки или default
    """
    return ALL_ICONS.get(name, default or f"{BASE_URL}/default.png")


def get_category_icons(category: str) -> dict:
    """
    Получить все иконки категории
    
    Args:
        category: Название категории
    
    Returns:
        Словарь с иконками категории
    """
    categories = {
        "class_etc": CLASS_ETC,
        "promotion": PROMOTION,
        "skills": SKILLS,
        "spirit": SPIRIT,  # Было spirit_familiars
        "info": INFO_CATEGORIES,
        "adventures": ADVENTURES,
        "guild": GUILD,
    }
    return categories.get(category, {})


def list_all_icons() -> list:
    """
    Получить список всех доступных имён иконок
    
    Returns:
        Список имён иконок
    """
    return list(ALL_ICONS.keys())


def generate_icon_html(name: str, size: int = 32) -> str:
    """
    Сгенерировать HTML для иконки
    
    Args:
        name: Имя иконки
        size: Размер в пикселях
    
    Returns:
        HTML строка с img тегом
    """
    url = get_icon(name)
    return f'<img src="{url}" alt="{name}" width="{size}" height="{size}" style="vertical-align: middle;">'


# ═══════════════════════════════════════════════════════
# 📊 СТАТИСТИКА
# ═══════════════════════════════════════════════════════

def get_stats() -> dict:
    """
    Получить статистику иконок
    
    Returns:
        Словарь со статистикой
    """
    return {
        "total_icons": len(ALL_ICONS),
        "class_etc": len(CLASS_ETC),
        "promotion": len(PROMOTION),
        "skills": len(SKILLS),
        "spirit": len(SPIRIT),  # Было spirit_familiars
        "info": len(INFO_CATEGORIES),
        "adventures": len(ADVENTURES),
        "guild": len(GUILD),
    }


# ═══════════════════════════════════════════════════════
# 🎨 ПРЕОБРАЗОВАНИЕ ЭМОДЗИ В ИКОНКИ
# ═══════════════════════════════════════════════════════

EMOJI_TO_ICON = {
    "🔷": "promo_ether",
    "⚔️": "promo_black_mithril",
    "🟩": "promo_demonite",
    "🐲": "promo_dragonos",
    "🔮": "promo_blood",
    "🥶": "promo_frost",
    "😈": "promo_nox",
    "🌊": "promo_abyss",
    "🔴": "promo_infinat",
    "🌪": "promo_cyclone",
    "🐉": "promo_ancient",
    "🗿": "promo_gigalor",
    "🪨": "cat_promoutes",
    "📜": "info_general",
    "🌳": "adv_adventures",
    "🛡": "guild_guild",
    "👻": "info_event",
    "😤": "info_rage",
    "📺": "info_ads",
    "🐾": "info_pets",
    "💰": "info_farm",
    "🕳️": "adv_cave",
    "🌀": "adv_rift",
    "🔥": "adv_shelter",
    "🪙": "adv_mind",
    "🌲": "adv_forest",
    "🍲": "guild_cooking",
}


def emoji_to_icon_url(emoji: str) -> str:
    """
    Преобразовать эмодзи в URL иконки
    
    Args:
        emoji: Эмодзи
    
    Returns:
        URL иконки или None
    """
    icon_name = EMOJI_TO_ICON.get(emoji)
    if icon_name:
        return get_icon(icon_name)
    return None