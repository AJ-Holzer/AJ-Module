import locale

def get_sys_language() -> str | None:
    """Return the system language.
    :return (str | None) language: (e.g. 'en' for English) if language found. Else None"""
    # Get the current locale setting
    lang, _ = locale.getlocale()
    # Return the language code (first part of the locale)
    return lang.split('_')[0] if lang else None  # Default to 'en' if locale is not set
