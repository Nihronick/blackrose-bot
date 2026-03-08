# ═══════════════════════════════════════════════════════
# 📋 КАТЕГОРИИ (с иконками)
# ═══════════════════════════════════════════════════════
MAIN_CATEGORIES = {
    "cat_promoutes": {
        "title": "Промоуты",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/cat_promoutes.png"
    },
    "info_general": {
        "title": "Общая информация",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/info_general.png"
    },
    "adv_adventures": {
        "title": "Приключения",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/adv_adventures.png"
    },
    "guild_guild": {
        "title": "Гильдия",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/guild_guild.png"
    }
}

# ═══════════════════════════════════════════════════════
# 📂 ПОДКАТЕГОРИИ (с иконками)
# ═══════════════════════════════════════════════════════
SUBMENUS = {
    "cat_promoutes": [
        ("promo_ether", "Эфир", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Ether.png"),
        ("promo_black_mithril", "Чёрный Мифрил", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/promo_black_mithril.png"),
        ("promo_demonite", "Демонит", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Demon Metal.png"),
        ("promo_dragonos", "Драгонос", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Dragonos.png"),
        ("promo_blood", "Кровь Великих", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Ragnablood.png"),
        ("promo_frost", "Иней Войны", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Warfrost.png"),
        ("promo_nox", "Тёмный Нокс", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Dark Nox.png"),
        ("promo_abyss", "Синяя Бездна", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Blue Abyss.png"),
        ("promo_infinat", "Инфинат", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Infinaut.png"),
        ("promo_cyclone", "Циклон", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Cyclos.png"),
        ("promo_ancient", "Эйшенткенаин", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Ancient Canine.png"),
        ("promo_gigalor", "Гигалор", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Gigarock.png"),
    ],
    "info_general": [
        ("info_event", "Что покупать на ивенте?", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/info_event.png"),
        ("info_rage", "Как играть с Яростью?", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/info_rage.png"),
        ("info_ads", "Просмотр рекламы", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/info_ads.png"),
        ("info_pets", "Прокачка спутников", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/info_pets.png"),
        ("info_sword", "Меч душ и гравировка", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/info_sword.png"),
        ("info_farm", "Фарм этапов", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/info_farm.png"),
        ("info_spirit", "Духи/Spirits", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/info_spirit.png"),
    ],
    "adv_adventures": [
        ("adv_cave", "Учебная пещера", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/adv_cave.png"),
        ("adv_rift", "Межпространственный разлом", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/adv_rift.png"),
        ("adv_shelter", "Приют Спящего Пламени", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/adv_shelter.png"),
        ("adv_mind", "Золотой рудник", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/adv_mind.png"),
        ("adv_forest", "Лес циркуляции", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/adv_forest.png"),
    ],
    "guild_guild": [
        ("guild_wyvern", "Виверна", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/guild_wyvern.png"),
        ("guild_cooking", "Приготовление блюд", "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/guild_cooking.png"),
    ]
}

# ═══════════════════════════════════════════════════════
# 📚 ГАЙДЫ (с иконками)
# 💡 ЗАМЕНЯЙТЕ "photo" НА URL (Imgur, Яндекс Диск, GitHub)
# ═══════════════════════════════════════════════════════
CONTENT = {
    # 🪨 ПРОМОУТЫ
    "promo_ether": {
        "title": "Эфир | Ether",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Ether.png",
        "text": """🔷 **Гайд на Эфир | Ether** 🔷

📊 **Характеристики:**
• Ориентировочный этап: 340 ± 5
• Атака: 100f (с 10 слотами и Яростью меньше)
• Крит. урон: 20а
• ДС: 3000
• Класс: с17-19
• Меч: м1 или opp
• Реликвии: 30-40

💎 **Спутники:**
• Навык Элли на понижение ОЗ: 30-40

👻 **Духи:**
• Noah, Loar, Sala: 1-3⭐

💡 **Советы:**
• Фокус на атаке и критическом уроне
• Оптимально для этапа 340""",
        "photo": [],  # 🔽 ЗАМЕНИТЕ НА URL: ["https://i.imgur.com/abc123.png"]
        "video": None,
        "document": None
    },
    
    "promo_black_mithril": {
        "title": "Чёрный Мифрил | Black Mythril",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/promo_black_mithril.png",
        "text": """⚔️ **Гайд на Чёрный Мифрил** ⚔️

📊 **Характеристики:**
• Ориентировочный этап: 460 ± 5
• Атака: 1.7-2g
• Крит. урон: 25-28а
• ДС: 4500-4800
• Класс: с17-19
• Меч: базовый орр
• Реликвии: 40-50

💎 **Спутники:**
• Уровень понижения ХР мобов: 45+
• Песня эльфов

👻 **Духи:**
• Noah: 3⭐-5⭐, E3-5
• Loar: 3⭐-5⭐, E3-5
• Sala: миф, E1-2

💡 **Советы:**
• С Бредом у Sala можно больше E1""",
        "photo": [],  # 🔽 Добавьте URL
        "video": None,
        "document": None
    },
    
    "promo_demonite": {
        "title": "Демонит | Demon Metal",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Demon Metal.png",
        "text": """ **Гайд на Демонит** 

📊 **Характеристики:**
• Ориентировочный этап: 550 ± 5
• Атака: 60-65g
• Крит. урон: 30-34а
• ДС: 5000-5200
• Класс: с18-19
• Меч: Базовый орр 3-5⭐
• Реликвии: 40-50

💎 **Спутники:**
• Навык Элли на понижение ХР мобов: 50+

👻 **Духи:**
• Noah: 3⭐-миф, E3-5
• Loar: 3⭐-5⭐, E3-5
• Sala: миф, E1-2

💎 **Камни навыков:**
• Вода, Камень, Огонь""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "promo_dragonos": {
        "title": "Драгонос | Dragonos",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Dragonos.png",
        "text": """🐲 **Гайд на Драгонос** 🐲

📊 **Характеристики:**
• Ориентировочный этап: 610 ± 5
• Атака: 250-300g с орбом, без 700g
• ХР: 4g
• Крит. урон: 32-37а
• ДС: 5800-6200
• Класс: с19, 20 без орба
• Меч: Базовый орр 3-5⭐ (Первый Авакен орра)
• Реликвии: 50-60

💎 **Спутники:**
• Навык Элли на понижение ОЗ врагов: 50+

👻 **Духи:**
• Noah: миф, E4-5
• Loar: миф, E4-5
• Sala: миф, E1-5

💎 **Камни навыков:**
• Вода, Камень, Огонь

⚔️ **Урон стихий:**
• Огня и камня: 3-4к""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "promo_blood": {
        "title": "Кровь Великих | Ragna Blood",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Ragnablood.png",
        "text": """🔮 **Гайд на Кровь Великих** 🔮

📊 **Характеристики:**
• Ориентировочный этап: 700 ± 5
• Атака: 9h
• Крит. урон: 35-40а
• ДС: 8000-8400
• Класс: с20 0-3⭐
• Меч: Базовый орр 5⭐ / Первый Авакен орра 0-4⭐
• Реликвии: 50-60

💎 **Спутники:**
• Эльфийская песня: 70-80 лвл
• Мудрость войны: 40-50

👻 **Духи:**
• Noah: миф, E4-5
• Loar: миф, E4-5
• Sala: миф, E3-5

⚔️ **Урон стихий:**
• Огня и Камня: 6-8к

💎 **Камни навыков:**
• Вода, Камень, Огонь""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "promo_frost": {
        "title": "Иней Войны | War Frost",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Warfrost.png",
        "text": """🥶 **Гайд на Иней Войны** 🥶

📊 **Характеристики:**
• Ориентировочный этап: 770 ± 5
• Атака: 156h
• ХР/Rxh: минимум 630g/30g
• Крит. урон: 63-67а
• ДС: 12000-12500
• Класс: с20 2-5⭐
• Меч: Первый Авакен орра 3-5⭐ → Абсолют
• Реликвии: 60-70

💎 **Спутники:**
• Эльфийская песня: 70+
• Мудрость войны: 50+

👻 **Духи:**
• Noah, Loar, Sala: все миф, E4-5

🐾 **Фамильяр:**
• Необязательно, но делается дешево: 6⭐6⭐6⭐ или 7⭐7⭐7⭐
• Хи/Ти Ку На

💎 **Камни навыков:**
• Вода, Земля, Огонь""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "promo_nox": {
        "title": "Тёмный Нокс | Dark Nox",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Dark Nox.png",
        "text": """😈 **Гайд на Тёмный Нокс** 😈

📊 **Характеристики:**
• Ориентировочный этап: 850 ± 5
• Атака: 4i
• Крит. урон: 72а
• ДС: 18500-19500
• Класс: терра 0-5⭐
• Меч: Первый авакен орра 3-5⭐ → Абсолют 0-3⭐
• Реликвии: 60-70

💎 **Спутники:**
• Эльфийская песня: 80+
• Мудрость войны: 60+

👻 **Духи:**
• Noah, Loar, Sala: все миф, E5

🐾 **Фамильяр:**
• ХИКУНА/ХИКУРИОН: 7⭐7⭐7⭐

💎 **Камни навыков:**
• Вода, Камень, Огонь

💡 **Важно:**
На этом промоуте игроки могут делать больший упор в меч или в класс. Если у вас условный сид, то меч будет хуже. Также с реликвиями: если меньше крита, то больше атаки. Не обязательно делать всё так же!""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "promo_abyss": {
        "title": "Синяя Бездна | Blue Abyss",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Blue Abyss.png",
        "text": """🌊 **Гайд на Синюю Бездну** 🌊

📊 **Характеристики:**
• Ориентировочный этап: 955 ± 5
• Атака и крит.урон: ~150i с 200а ИЛИ 180-200i с 150а
• ХР: минимум 310h и около 18h РХР
• ДС: 29000-31000
• Класс: терра 3-5⭐, сид
• Меч: Первый Абсолют 3-5⭐ → Абсолют v2
• Реликвии: 80-100

💎 **Спутники:**
• Эльфийская песня: 100 лвл
• Мудрость войны: 80+

👻 **Духи:**
• Noah, Loar, Sala: все миф, E5

🐾 **Фамильяр:**
• ХИКУНА/ХИКУРИОН: 7⭐

⚔️ **Элементальный урон:**
• Огня: 14-15а

💎 **Камни навыков:**
• Вода, Камень, Огонь""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "promo_infinat": {
        "title": "Инфинат | Inflnat",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Infinaut.png",
        "text": """🔴 **Гайд на Инфинат** 🔴

📊 **Характеристики:**
• Ориентировочный этап: 1020 ± 5
• Атака: 3.5j-3.7j
• ХР/Rxh: 4.5i/230h
• Крит. урон: 210а-220а
• ДС: 30000-35000
• Класс: сид 0-5⭐
• Меч: Второй Абсолют 3-5⭐ → Меч древних
• Реликвии: крит, урон 100

💎 **Спутники:**
• Эльфийская песня: 100 лвл
• Мудрость войны: 100 лвл

👻 **Духи:**
• Noah, Loar, Sala: все миф, E5

🐾 **Фамильяр:**
• ХИКУНА/ХИКУРИОН: 7⭐

⚔️ **Элементальный урон:**
• Огня: 18а+
• Земли: 15а+

💎 **Камни навыков:**
• Вода, Камень, Огонь

💡 **Примечание:**
У кого-то может быть наоборот: есть нова, но нет фулл меча""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "promo_cyclone": {
        "title": "Циклон | Ciclos",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Cyclos.png",
        "text": """🌪 **Гайд на Циклон** 🌪

📊 **Характеристики:**
• Ориентировочный этап: 1120 ± 5
• Атака: 290j-320j
• Крит. урон: 235а-245а
• ДС: 48000-53000
• Класс: сид 3-5⭐, нова
• Меч: Абсолют V2 3-5⭐ → Меч древних
• Реликвии: крит, урон 100

💎 **Спутники:**
• Эльфийская песня: 100 лвл
• Мудрость войны: 100 лвл

👻 **Духи:**
• Noah, Loar, Sala: все миф, E5

🐾 **Фамильяр:**
• ХИКУНА/ХИКУРИОН: 7⭐

⚔️ **Элементальный урон:**
• Огня и Камня: 30а-33а

💎 **Камни навыков:**
• Вода, Камень, Огонь""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "promo_ancient": {
        "title": "Эйшенткенаин | Ancient Canine",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Ancient Canine.png",
        "text": """🐉 **Гайд на Эйшенткенаин** 🐉

⚠️ **Дисклеймер:**
Урон, получаемый из статов ниже, непосредственно связан с самой проходкой. При других прожатиях может понадобиться больше урона.

📊 **Характеристики:**
• Ориентировочный этап: 1210 ± 5
• Без фамика 8⭐8⭐8⭐ проходится уже на 1200
• Атака: 8.5k-9k
• Крит. урон: 280а-300а
• ДС: 70000-75000
• Класс: сид 4-5⭐, нова
• Меч: Абсолют V2 4-5⭐ → Меч древних
• Реликвии: 100 крит, урон

💎 **Спутники:**
• Эльфийская песня: 100
• Мудрость войны: 100

👻 **Духи:**
• Sala (в первом слоте!), Noah, Loar: все миф 2-5⭐, либо иммортал, E5

🐾 **Фамильяр:**
• Так как босс имеет стихию Огня, желательно иметь А (фамильяр)
• Или ХИКУНА: все 7⭐ и выше

💎 **Камни навыков:**
• Вода, Камень, Ветер

⚔️ **Элементальный урон:**
• Огня: 35-40а
• Ветра: 30а+
• Воды: 25а+ (если используете А)
• Земли: 35-40а (если используете Охоту на демонов)""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "promo_gigalor": {
        "title": "Гигалор | Gigarock",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/Gigarock.png",
        "text": """🗿 **Гайд на Гигалор** 🗿

📊 **Характеристики:**
• Ориентировочный этап: 1300 ± 5
• Атака: 350k с яростью / 380k без ярости
• ХР/Rxh: если без ярости - неважно / с яростью желательно более 500g
• Крит. урон: 350а-370а
• ДС: 100000+
• Класс: нова
• Меч: Древний
• Реликвии: 100

💎 **Спутники:**
• Эльфийская песня: 100 лвл
• Мудрость войны: 100 лвл

👻 **Духи:**
• Noah, Loar, Sala: все миф-имм, E5

🐾 **Фамильяр:**
• ХИКУНА: 8⭐, 8⭐, 8⭐

💎 **Камни навыков:**
• Вода, Земля, Огонь

💡 **Примечание:**
Статы максимально примерные! У кого-то может не быть 8 фамильяра или высокого уровня 🔥 или других баффающих навыков.""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    # 📜 ОБЩАЯ ИНФОРМАЦИЯ
    "info_event": {
        "title": "Что покупать на ивенте?",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/info_event.png",
        "text": """👻 **Что покупать на ивенте?**

📌 **Приоритет 1:** Легендарный дух

📌 **Приоритет 2:** 3 эпических духа

📌 **Приоритет 3:** До черного мифрила можете покупать легендарный навык
• Медитация
• Адский удар
• Ярость

📌 **Приоритет 4:** Бери навыки РЕДКИЕ (приоритет будет на картинке)

📌 **Приоритет 5:** Зеленые перья и фиолетовые
• Только в том случае, когда редкие навыки уже заполнены

❗️ **Важно:**
Не стоит менять на АЛМАЗЫ, только покупка по приоритету!""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "info_rage": {
        "title": "Как играть с Яростью?",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/info_rage.png",
        "text": """😤 **Как играть с Яростью?**

🎥 **Обучающее видео:**
Смотрите на тайминги нажатия кнопок

💡 **Советы:**
• Следите за временем активации
• Используйте в нужный момент
• Комбинируйте с другими навыками""",
        "photo": [],
        "video": [],  # 🔽 Добавьте URL видео
        "document": None
    },
    
    "info_ads": {
        "title": "Просмотр рекламы",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/info_ads.png",
        "text": """📺 **Просмотр рекламы**

💰 **Стоимость:**
• VPN: 500-700 рублей на покупку скипа

📱 **Инструкция:**
1. Включите VPN
2. Откройте раздел рекламы
3. Просмотрите рекламу для получения бонусов

💡 **Альтернатива:**
Можно смотреть рекламу без VPN, но с ограничениями""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "info_pets": {
        "title": "Прокачка спутников",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/info_pets.png",
        "text": """🐾 **Прокачка спутников**

⭐ **Приоритет прокачки:**
Качайте по приоритету, указанному в гайдах. Спутники со звездой нужно качать в первую очередь!

💎 **Души:**
На ваше усмотрение, какой меч хотите получать.

📊 **Рекомендации:**
• Фокусируйтесь на основных спутниках
• Не распыляйте ресурсы
• Следуйте приоритетам из гайдов""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "info_sword": {
        "title": "Меч душ и гравировка",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/info_sword.png",
        "text": """⚔️ **Меч душ и гравировка**

💎 **Рекомендации по самоцветам:**

1. **Отдавайте предпочтение высокоуровневым самоцветам Души**
   • Увеличивают коэффициент полезного действия оружия

2. **Выбирайте самоцветы более высокой редкости**
   • Эпические, легендарные, мифические
   • Более мощные дополнительные возможности

3. **Собирайте драгоценные камни ATK (L-образной формы)**
   • Не забывайте заполнять игровое поле

4. **Золотые блоки (I-образной формы)**
   • В начале и середине игры
   • Значительно увеличивают процент золота

📊 **Стратегия:**
Сохраните 2 набора гравюр:
• 1 для увеличения золота (во время фарминга)
• 1 для увеличения урона (во время толкания стадии)

🎯 **Поздняя игра (1500+):**
Оружие Души может отдавать предпочтение критическим блокам""",
        "photo": [],
        "video": None,
        "document": []  # 🔽 Добавьте URL документов
    },
    
    "info_farm": {
        "title": "Фарм этапов",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/info_farm.png",
        "text": """💰 **Фарм этапов**

📊 **Наиболее важные этапы:**

**4 MPW (мобов в минуту):**
• Хороши для получения опыта и золота
• Меньше мобов = меньше время прохождения
• Можно проходить более высокие уровни

**18 MPW:**
• Хороши для сбора кубов, душ, снаряжения и алмазов
• Время прохождения: 36-42 секунды
• Больше монстров = больше ресурсов

🌐 **Онлайн vs Оффлайн:**

✅ **Онлайн-фарм ЛУЧШЕ:**
1. Ограниченное время оффлайна (10 часов)
2. Получаете бриллианты за ежедневные задания
3. Получаете снаряжение
4. Выше стоимость кубов и душ

⚠️ **Оффлайн-фарм (для новичков):**
• После 160 этапа только 4 и 18 MPW
• Нельзя выбирать где фармить""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "info_spirit": {
        "title": "Духи/Spirits",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/info_spirit.png",
        "text": """👻 **Духи - Оптимизация**

📌 **Ранняя игра:**

**Цель:** Два духа с высоким пробуждением (A6) + два с хорошими множителями навыков

**Принцип:**
• Характеристики 3-х духов усредняются
• 2 высоко пробужденных компенсируют третьего

**Берем по 1 духу из каждого элемента:**
• 🔥 Огонь
• 🌍 Земля
• 💨 Ветер
• 💧 Вода

🎯 **Середина игры (12/12 Мифических):**

**Приоритет пробуждения Бессмертных:**

🔥 **Огонь:**
Sala A6 → Mum E5 → Mum A6 → Bo A6 → Mum A12 → Sala E5 → Sala A12 → A12 Bo → A18 Mum → A18 Sala

🌍 **Земля:**
Loar A6E5 → Noah E5 → Noah A6 → Radon A6 → Noah A12 → Loar A12 → A12 Radon → A18 Noah → A18 Loar

💨 **Ветер:**
Zappy A6E5 → Kart A6 → Herh A6 → Zappy A12 → Kart E5 → A12 Kart → A12 Herh → A18 Zappy

💧 **Вода:**
Todd E5 → Todd A6 → Luga A6 → Ark A6 → Luga E5 → Luga A12/Todd A12 → A12 Ark → A18 Luga → A18 Todd

📌 **Источник циркуляции:**

**Основные (поднимаем уровень):**
Noah, Zappy, Loar, Todd, Radon, Mum

**Присоединяем к фонтану:**
Nerh, Ark, Boo, Kart, Sala, Luga

❗️ **Пробуждение:**
После 12/12 Мифических духов выбирайте вариант с 4 равными полосами. Статистика повышается на 20%!""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    # 🌳 ПРИКЛЮЧЕНИЯ
    "adv_cave": {
        "title": "Учебная пещера",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/adv_cave.png",
        "text": """🕳️ **Учебная пещера**

📍 **Описание:**
Начальная зона для обучения и фарма

🎯 **Рекомендации:**
• Идеально для новичков
• Быстрый фарм опыта
• Простые враги""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "adv_rift": {
        "title": "Межпространственный разлом",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/adv_rift.png",
        "text": """🌀 **Межпространственный разлом**

📍 **Описание:**
Продвинутая зона для фарма

🎯 **Рекомендации:**
• Требует подготовки
• Хорошие награды
• Сложные враги""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "adv_shelter": {
        "title": "Приют Спящего Пламени",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/adv_shelter.png",
        "text": """🔥 **Приют Спящего Пламени**

📍 **Описание:**
Зона с огненной стихией

🎯 **Рекомендации:**
• Подготовьте защиту от огня
• Используйте водные навыки
• Ценные ресурсы""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "adv_mind": {
        "title": "Золотой рудник",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/adv_mind.png",
        "text": """🪙 **Золотой рудник**

📊 **Стратегия фарма:**

**Зоны 1-4:**
• Используйте 3 пера
• Уничтожайте 90-95% врагов
• Сложнее всего с землей (навыки фарминга - ветер)

**Зона 2:**
• Лучшая для фарма
• Больше опыта чем в зоне 1

**Зона 5:**
• Хуже для фарма
• Меньше мобов

🎯 **Рекомендации:**
• Фармите нечетные этажи (ресурсы увеличиваются)
• После 250 этажа: выделяйте 4n+1 этаж
• Лучшее время: ежедневные свитки + горячее время выходных + бонусы событий
• Получайте 12-кратное золото и 6-кратный опыт

💡 **Совет:**
Используйте обычную ежедневную прокрутку кубов - получаете больше кубов от мобов""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "adv_forest": {
        "title": "Лес циркуляции",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/adv_forest.png",
        "text": """🌲 **Лес циркуляции**

📍 **Описание:**
Зона для фарма духов циркуляции

🎯 **Рекомендации:**
• Фокусируйтесь на основных духах
• Собирайте ресурсы
• Используйте правильную стихию""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    # 🛡 ГИЛЬДИЯ
    "guild_wyvern": {
        "title": "Виверна",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/guild_wyvern.png",
        "text": """🐉 **Виверна - Гильдейское событие**

📋 **Этапы:**
1. Фарм ресурсов и готовка
2. Битва с Виверной

🏆 **Почему это важно:**

**Индивидуальные награды:**
• Зависят от ранга гильдии
• Чем выше гильдия - тем больше ресурсов

**Вклад:**
• Готовка
• Битва с виверной

💡 **Советы:**
• Участвуйте активно
• Готовьте блюда заранее
• Координируйтесь с гильдией""",
        "photo": [],
        "video": None,
        "document": None
    },
    
    "guild_cooking": {
        "title": "Приготовление блюд",
        "icon": "https://raw.githubusercontent.com/Nihronick/blackrose-bot/main/public/images/icons/guild_cooking.png",
        "text": """🍲 **Приготовление блюд**

📌 **Приоритет еды:**
(Определяется ГМ, меняется каждый сезон)

🍖 **Типы блюд:**

**9-ка (приоритет 1):**
• Дает больше ресурсов в дальнейшем фарме
• Готовится первоочередно

**Шашлык:**
• Увеличивает время действия баффа

**Омурис:**
• Увеличивает время боя в рейде

**Фруктовый салат / Жевательная паста:**
• Уменьшает время восстановления навыка

**Бессмертный стейк:**
• Увеличивает урон от виверн

**Бонусы стихий:**
• Определите приоритетные элементы
• Огонь и земля для большинства игроков

💡 **Совет:**
Следуйте указаниям ГМ каждый сезон!""",
        "photo": [],
        "video": None,
        "document": None
    },
}

# ═══════════════════════════════════════════════════════
# 📊 СТАТИСТИКА
# ═══════════════════════════════════════════════════════
def get_stats():
    """Получить статистику гайдов"""
    total_guides = len(CONTENT)
    total_categories = len(MAIN_CATEGORIES)
    total_photos = sum(len(guide.get("photo", []) or []) for guide in CONTENT.values())
    total_videos = sum(len(guide.get("video", []) or []) for guide in CONTENT.values())
    total_documents = sum(len(guide.get("document", []) or []) for guide in CONTENT.values())
    
    return {
        "total_guides": total_guides,
        "total_categories": total_categories,
        "total_photos": total_photos,
        "total_videos": total_videos,
        "total_documents": total_documents,
        "guides_with_photos": sum(1 for guide in CONTENT.values() if guide.get("photo")),
        "guides_with_videos": sum(1 for guide in CONTENT.values() if guide.get("video")),
    }