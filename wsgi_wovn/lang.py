class Lang(object):
    LANG = {
        'ar': {
            'name': 'ﺎﻠﻋﺮﺒﻳﺓ',
            'code': 'ar',
            'en': 'Arabic'
        },
        'zh-CHS': {
            'name': '简体中文',
            'code': 'zh-CHS',
            'en': 'Simp Chinese'
        },
        'zh-CHT': {
            'name': '繁體中文',
            'code': 'zh-CHT',
            'en': 'Trad Chinese'
        },
        'da':     {
            'name': 'Dansk',
            'code': 'da',
            'en': 'Danish'
        },
        'nl':     {
            'name': 'Nederlands',
            'code': 'nl',
            'en': 'Dutch'
        },
        'en':     {
            'name': 'English',
            'code': 'en',
            'en': 'English'
        },
        'fi':     {
            'name': 'Suomi',
            'code': 'fi',
            'en': 'Finnish'
        },
        'fr':     {
            'name': 'Français',
            'code': 'fr',
            'en': 'French'
        },
        'de':     {
            'name': 'Deutsch',
            'code': 'de',
            'en': 'German'
        },
        'el':     {
            'name': 'Ελληνικά',
            'code': 'el',
            'en': 'Greek'
        },
        'he':     {
            'name': 'עברית',
            'code': 'he',
            'en': 'Hebrew'
        },
        'id':     {
            'name': 'Bahasa Indonesia',
            'code': 'id',
            'en': 'Indonesian'
        },
        'it':     {
            'name': 'Italiano',
            'code': 'it',
            'en': 'Italian'
        },
        'ja':     {
            'name': '日本語',
            'code': 'ja',
            'en': 'Japanese'
        },
        'ko':     {
            'name': '한국어',
            'code': 'ko',
            'en': 'Korean'
        },
        'ms':     {
            'name': 'Bahasa Melayu',
            'code': 'ms',
            'en': 'Malay'
        },
        'no':     {
            'name': 'Norsk',
            'code': 'no',
            'en': 'Norwegian'
        },
        'pl':     {
            'name': 'Polski',
            'code': 'pl',
            'en': 'Polish'
        },
        'pt':     {
            'name': 'Português',
            'code': 'pt',
            'en': 'Portuguese'
        },
        'ru':     {
            'name': 'Русский',
            'code': 'ru',
            'en': 'Russian'
        },
        'es':     {
            'name': 'Español',
            'code': 'es',
            'en': 'Spanish'
        },
        'sv':     {
            'name': 'Svensk',
            'code': 'sv',
            'en': 'Swedish'
        },
        'th':     {
            'name': 'ภาษาไทย',
            'code': 'th',
            'en': 'Thai'
        },
        'hi':     {
            'name': 'हिन्दी',
            'code': 'hi',
            'en': 'Hindi'
        },
        'tr':     {
            'name': 'Türkçe',
            'code': 'tr',
            'en': 'Turkish'
        },
        'uk':     {
            'name': 'Українська',
            'code': 'uk',
            'en': 'Ukrainian'
        },
        'vi':     {
            'name': 'Tiếng Việt',
            'code': 'vi',
            'en': 'Vietnamese'
        },
    }

    @classmethod
    def get_code(cls, lang_name):
        if not lang_name:
            return None

        if lang_name in cls.LANG:
            return lang_name

        for k, v in cls.LANG.items():
            if lang_name.lower() == v['name'].lower() \
                    or lang_name.lower() == v['en'].lower() \
                    or lang_name.lower() == v['code'].lower():
                return v['code']

        return None

    @classmethod
    def get_lang(cls, lang):
        lang_code = cls.get_code(lang)
        return cls.LANG.get(lang_code)
