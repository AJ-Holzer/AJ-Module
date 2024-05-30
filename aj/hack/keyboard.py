import keyboard as kb

def block_keyboard() -> None:
    """Blocks all keys of the keyboard. This module doesn't activate them later again! (You have to login to activate them again...)"""
    def get_all_keyboard_keys():
        # Druckbare ASCII-Zeichen
        printable_keys = [chr(key_code) for key_code in range(32, 127)] + ["ö", "ä", "ü"]
        
        # Funktionstasten
        function_keys = [f'F{i}' for i in range(1, 13)]
        
        # Andere Tasten
        other_keys = [
            'enter', 'tab', 'shift', 'ctrl', 'alt', 'backspace', 'delete',
            'home', 'end', 'page up', 'page down', 'up', 'down', 'left', 'right',
            'insert', 'esc', 'caps lock', 'num lock', 'scroll lock', "left windows",
            "right windows"
        ]

        special = [
            "alt",
            "linke windows",
            "strg",
            "umschalt",     
            "feststell",    
            "tab",
            "esc",
            "f1",
            "f2",
            "f3",
            "f4",
            "f5",
            "f6",
            "f7",
            "f8",
            "f9",
            "f10",
            "f11",
            "f12",
            "druck",
            "einfg",
            "entf",
            "backspace",
            "enter",
            "right shift",
            "nach-rechts",
            "nach-unten",
            "nach-links",
            "nach-oben",
            "strg-rechts",
            "alt gr",
            "space",
            "shift",
            "ctrl",
            "F1",
            "F2",
            "F3",
            "F4",
            "F5",
            "F6",
            "F7",
            "F8",
            "F9",
            "F10",
            "F11",
            "F12",
            "capslock",
            "delete",
            "insert",
            "home",
            "end",
            "pageup",
            "pagedown",
            "up",
            "down",
            "left",
            "right",
            "numlock",
            "pause",
            "menu",
            "select",
            "execute",
            "help",
            "application",
            "sleep",
            "volume_mute",
            "volume_down",
            "volume_up",
        ]
        
        all_keys = printable_keys + function_keys + other_keys + special
        return all_keys

    for i in get_all_keyboard_keys():
        try:
            kb.block_key(key= str(i))
        except Exception as e:
            pass