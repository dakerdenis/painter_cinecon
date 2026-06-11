from main.models.translation_string import Translation

translations = {
    "about.title": {
        "ru": "Обо мне",
        "en": "About Me",
        "az": "Haqqımda",
    },

    "about.hero.title": {
        "ru": "Окно в творчество",
        "en": "A Window into Creativity",
        "az": "Yaradıcılığa pəncərə",
    },

    "about.hero.subtitle": {
        "ru": "Раскрывая художественную историю Джейсона Кариага",
        "en": "Uncovering the Artistic Story of Jason Cariag",
        "az": "Jason Cariag-in bədii hekayəsini kəşf etmək",
    },

    "about.welcome": {
        "ru": "Добро пожаловать в мой художественный мир!",
        "en": "Welcome to my artistic world!",
        "az": "Mənim sənət dünyama xoş gəlmisiniz!",
    },

    "about.intro": {
        "ru": "Я Джейсон Крейг, увлечённый художник и визуальный рассказчик. Через живопись я стремлюсь передать суть эмоций, моментов и красоты, которая нас окружает. Искусство всегда было моим языком самовыражения.",
        "en": "I am Jason Craig, a passionate painter and visual storyteller. Through the medium of paint, I strive to capture the essence of emotions, moments, and the beauty that surrounds us. Art has always been my language of expression, allowing me to convey ideas and perspectives that words often fail to capture.",
        "az": "Mən Jason Craigəm, həvəsli rəssam və vizual hekayəçiyəm. Rənglər vasitəsilə duyğuların, anların və ətrafımızdakı gözəlliyin mahiyyətini çatdırmağa çalışıram. Sənət həmişə mənim özümü ifadə dilim olub.",
    },

    "about.inspiration": {
        "ru": "Вдохновлённые игрой света и тени, нюансами цветов и глубиной человеческого опыта, мои картины ведут зрителя к размышлению и внутреннему созерцанию. Каждый мазок — это возможность передать мои мысли и чувства и пригласить вас увидеть мир моими глазами.",
        "en": "Inspired by the interplay of light and shadow, the nuances of colors, and the depth of human experiences, my paintings take viewers on a journey of contemplation and introspection. Each brushstroke is an opportunity for me to communicate my thoughts and feelings, and to invite you to see the world through my eyes.",
        "az": "İşıq və kölgənin qarşılıqlı oyunu, rənglərin incəlikləri və insan təcrübələrinin dərinliyi mənə ilham verir. Rəsmlərim tamaşaçını düşüncə və daxili müşahidə səyahətinə aparır. Hər fırça toxunuşu fikirlərimi və hisslərimi çatdırmaq üçün bir fürsətdir.",
    },

    "about.signature": {
        "ru": "Изображение подписи",
        "en": "Signature image",
        "az": "İmza şəkli",
    },

    "about.move.text": {
        "ru": "ЖИВОПИСЬ ЦИФРОВАЯ ИЛЛЮСТРАЦИЯ СВЕТ КОЛЛАБОРАЦИЯ МАТОВАЯ ЖИВОПИСЬ",
        "en": "PAINTING DIGITAL ILLUSTRATION LIGHTING COLLABORATION MATTE PAINTING",
        "az": "RƏSSAMLIQ RƏQƏMSAL İLLUSTRASİYA İŞIQ ƏMƏKDAŞLIQ MAT RƏSSAMLIQ",
    },

    "about.award.title": {
        "ru": "ПРЕМИЯ ЗА ВКЛАД ВСЕЙ ЖИЗНИ",
        "en": "LIFETIME ACHIEVEMENT AWARD",
        "az": "ÖMÜR BOYU NAİLİYYƏT MÜKAFATI",
    },

    "about.award.organization": {
        "ru": "Национальная ассоциация художников, Баку",
        "en": "National Asssociation of Artists, Baku",
        "az": "Rəssamlar Milli Assosiasiyası, Bakı",
    },

    "about.award.country": {
        "ru": "Азербайджан",
        "en": "Azerbaijan",
        "az": "Azərbaycan",
    },

    "about.stats.projects": {
        "ru": "Завершённых проектов",
        "en": "Projects completed",
        "az": "Tamamlanmış layihələr",
    },

    "about.stats.experience": {
        "ru": "Лет опыта",
        "en": "Years of Experience",
        "az": "Təcrübə illəri",
    },

    "about.stats.books": {
        "ru": "Опубликованных арт-книг",
        "en": "Art Books Published",
        "az": "Nəşr edilmiş sənət kitabları",
    },
}

for key, value in translations.items():
    Translation.objects.update_or_create(
        key=key,
        defaults={
            "text_ru": value["ru"],
            "text_en": value["en"],
            "text_az": value["az"],
        }
    )

print(f"Loaded {len(translations)} about translations")