"""
BlackRose Mini App - Управление иконками
"""

from urllib.parse import quote

# ═══════════════════════════════════════════════════════
# БАЗОВЫЙ URL ДЛЯ ИЗОБРАЖЕНИЙ
# ═══════════════════════════════════════════════════════
BASE_URL = "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons"


def _url(path: str) -> str:
    """Безопасное формирование URL — кодирует пробелы и спецсимволы"""
    # Разбиваем путь на части и кодируем каждую
    parts = path.split("/")
    encoded_parts = [quote(part, safe="") for part in parts]
    return f"{BASE_URL}/{'/'.join(encoded_parts)}"


# ═══════════════════════════════════════════════════════
# CLASS_ETC (Классы, мечи, реликвии и прочее)
# ═══════════════════════════════════════════════════════
CLASS_ETC = {
    # Классы
    "class_c18": _url("class_etc/c18.png"),
    "class_c19": _url("class_etc/c19.png"),
    "class_terra": _url("class_etc/Tera.png"),
    "class_nova": _url("class_etc/Nova.png"),
    "class_sid": _url("class_etc/Seed.png"),
    # Мечи — пробелы теперь безопасно кодируются
    "sword_m1": _url("class_etc/m1 sword.png"),
    "sword_opp": _url("class_etc/orr.png"),
    "sword_orb": _url("class_etc/orb.png"),
    "sword_awaken": _url("class_etc/awaken.png"),
    "sword_absolutev1": _url("class_etc/AbsoluteV1.png"),
    "sword_absolutev2": _url("class_etc/AbsoluteV2.gif"),
    # Реликвии
    "relic_weapon": _url("class_etc/relic_weapon.png"),
    "relic_armor": _url("class_etc/relic_armor.png"),
    "relic_accessory": _url("class_etc/relic_accessory.png"),
    # Другое
    "stage": _url("class_etc/stage.png"),
    "ds": _url("class_etc/ds.png"),
    "attack": _url("class_etc/attack.png"),
    "crit_damage": _url("class_etc/crit_damage.png"),
    "hp": _url("class_etc/hp.png"),
    "rxp": _url("class_etc/rxp.png"),
    "check": _url("class_etc/check.png"),
    "cross": _url("class_etc/cross.png"),
    "warning": _url("class_etc/warning.png"),
    "info": _url("class_etc/info.png"),
    "star": _url("class_etc/star.png"),
    "diamond": _url("class_etc/diamond.png"),
    "gold": _url("class_etc/gold.png"),
    "gem": _url("class_etc/gem.png"),
}

# ═══════════════════════════════════════════════════════
# PROMOTION (Промоуты)
# ═══════════════════════════════════════════════════════
PROMOTION = {
    "promo_ether": _url("promotion/Ether.png"),
    "promo_black_mithril": _url("promotion/Black Mythril.png"),
    "promo_demonite": _url("promotion/Demon Metal.png"),
    "promo_dragonos": _url("promotion/Dragonos.png"),
    "promo_blood": _url("promotion/Ragnablood.png"),
    "promo_frost": _url("promotion/Warfrost.png"),
    "promo_nox": _url("promotion/Dark Nox.png"),
    "promo_abyss": _url("promotion/Blue Abyss.png"),
    "promo_infinat": _url("promotion/Infinaut.png"),
    "promo_cyclone": _url("promotion/Cyclos.png"),
    "promo_ancient": _url("promotion/Ancient Canine.png"),
    "promo_gigalor": _url("promotion/Gigarock.png"),
    "cat_promoutes": _url("promotion/cat_promoutes.png"),
}

# ═══════════════════════════════════════════════════════
# SKILLS (Навыки и камни)
# ═══════════════════════════════════════════════════════
SKILLS = {
    "skill_water": _url("skills/skill_water.png"),
    "skill_earth": _url("skills/skill_earth.png"),
    "skill_wind": _url("skills/skill_wind.png"),
    "skill_fire": _url("skills/skill_fire.png"),
    "skill_meditation": _url("skills/skill_meditation.png"),
    "skill_hell_strike": _url("skills/skill_hell_strike.png"),
    "skill_rage": _url("skills/skill_rage.png"),
    "skill_elf_song": _url("skills/skill_elf_song.png"),
    "skill_war_wisdom": _url("skills/skill_war_wisdom.png"),
    "element_fire": _url("skills/element_fire.png"),
    "element_earth": _url("skills/element_earth.png"),
    "element_wind": _url("skills/element_wind.png"),
    "element_water": _url("skills/element_water.png"),
}

# ═══════════════════════════════════════════════════════
# SPIRIT (Духи и фамильяры)
# ⚠️ Проверь в GitHub: папка "spirits" или "spirit"?
# ═══════════════════════════════════════════════════════
SPIRIT = {
    # Духи — папка "spirits"
    "spirit_noah": _url("spirits/Noah.png"),
    "spirit_loar": _url("spirits/Loar.png"),
    "spirit_sala": _url("spirits/Sala.png"),
    "spirit_mum": _url("spirits/Mum.png"),
    "spirit_bo": _url("spirits/Bo.png"),
    "spirit_radon": _url("spirits/Radon.png"),
    "spirit_zappy": _url("spirits/Zappy.png"),
    "spirit_kart": _url("spirits/Kart.png"),
    "spirit_herh": _url("spirits/Herh.png"),
    "spirit_todd": _url("spirits/Todd.png"),
    "spirit_luga": _url("spirits/Luga.png"),
    "spirit_ark": _url("spirits/Ark.png"),
    "spirit_nerh": _url("spirits/Nerh.png"),
    # Фамильяры — папка "spirit" (⚠️ другая папка!)
    "familiar_hikuna": _url("spirit/familiar_hikuna.png"),
    "familiar_hikurion": _url("spirit/familiar_hikurion.png"),
    "familiar_tikuna": _url("spirit/familiar_tikuna.png"),
    "familiar_a": _url("spirit/familiar_a.png"),
    # Звёзды
    "star_1": _url("spirit/star_1.png"),
    "star_3": _url("spirit/star_3.png"),
    "star_5": _url("spirit/star_5.png"),
    "star_6": _url("spirit/star_6.png"),
    "star_7": _url("spirit/star_7.png"),
    "star_8": _url("spirit/star_8.png"),
    "awaken_e": _url("spirit/awaken_e.png"),
    "awaken_a": _url("spirit/awaken_a.png"),
}

# ═══════════════════════════════════════════════════════
# КАТЕГОРИИ ИНФОРМАЦИИ
# ═══════════════════════════════════════════════════════
INFO_CATEGORIES = {
    "info_general": _url("info_general.png"),
    "info_event": _url("info_event.png"),
    "info_rage": _url("info_rage.png"),
    "info_ads": _url("info_ads.png"),
    "info_pets": _url("info_pets.png"),
    "info_sword": _url("info_sword.png"),
    "info_farm": _url("info_farm.png"),
    "info_spirit": _url("info_spirit.png"),
    "info_build": _url("info_build.png"),
}

# ═══════════════════════════════════════════════════════
# ПРИКЛЮЧЕНИЯ
# ═══════════════════════════════════════════════════════
ADVENTURES = {
    "adv_adventures": _url("adv_adventures.png"),
    "adv_cave": _url("adv_cave.png"),
    "adv_rift": _url("adv_rift.png"),
    "adv_shelter": _url("adv_shelter.png"),
    "adv_mind": _url("adv_mind.png"),
    "adv_forest": _url("adv_forest.png"),
}

# ═══════════════════════════════════════════════════════
# ГИЛЬДИЯ
# ═══════════════════════════════════════════════════════
GUILD = {
    "guild_guild": _url("guild_guild.png"),
    "guild_wyvern": _url("guild_wyvern.png"),
    "guild_cooking": _url("guild_cooking.png"),
}

# ═══════════════════════════════════════════════════════
# ВСЕ ИКОНКИ
# ═══════════════════════════════════════════════════════
ALL_ICONS = {
    **CLASS_ETC,
    **PROMOTION,
    **SKILLS,
    **SPIRIT,
    **INFO_CATEGORIES,
    **ADVENTURES,
    **GUILD,
}


# ═══════════════════════════════════════════════════════
# HELPER ФУНКЦИИ
# ═══════════════════════════════════════════════════════


def get_icon(name: str, default: str = None) -> str:
    """Получить URL иконки по имени. Возвращает None если не найдена."""
    return ALL_ICONS.get(name, default)


def get_category_icons(category: str) -> dict:
    """Получить все иконки категории"""
    categories = {
        "class_etc": CLASS_ETC,
        "promotion": PROMOTION,
        "skills": SKILLS,
        "spirit": SPIRIT,
        "info": INFO_CATEGORIES,
        "adventures": ADVENTURES,
        "guild": GUILD,
    }
    return categories.get(category, {})


def list_all_icons() -> list:
    """Список всех имён иконок"""
    return list(ALL_ICONS.keys())


def generate_icon_html(name: str, size: int = 32) -> str:
    """HTML тег для иконки"""
    url = get_icon(name)
    if not url:
        return ""
    return (
        f'<img src="{url}" alt="{name}" width="{size}" height="{size}" '
        f'class="inline-icon" onerror="this.style.display=\'none\'">'
    )


def get_stats() -> dict:
    """Статистика иконок"""
    return {
        "total_icons": len(ALL_ICONS),
        "class_etc": len(CLASS_ETC),
        "promotion": len(PROMOTION),
        "skills": len(SKILLS),
        "spirit": len(SPIRIT),
        "info": len(INFO_CATEGORIES),
        "adventures": len(ADVENTURES),
        "guild": len(GUILD),
    }
