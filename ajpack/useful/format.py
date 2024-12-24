from typing import Any

def table(dct: dict[Any, Any], sep: str = ":", align_l: str = "left", align_r: str = "left") -> str:
    """
    Creates a table of the given dictionary.
    sep: The character which seperates the left from the right side.
    align_l / align_r: left, right, centered

    :param dct: Dictionary to use (key: left side, value: right side).
    :param sep: The seperator to use.
    :param align_l: Where to align the left column.
    :param align_r: Where to align the right column.
    :return: str --> The table.
    """
    align: dict[str, str] = {
        "left": "<",
        "right": ">",
        "centered": "^"
    }
    tmp_lst: list[str] = []
    len1: int = 0
    len2: int = 0

    if not align_l in align.keys() or not align_r in align.keys(): raise ValueError("The given alignment doesn't exist!")

    for key, value in dct.items():
        if len(str(key)) > len1: len1 = len(str(key))
        if len(str(value)) > len2: len2 = len(str(value))

    for key, value in dct.items():
        tmp_lst.append(f"{str(key):{align[align_l]}{len1}} {sep} {str(value):{align[align_r]}{len2}}")
    
    return "\n".join(tmp_lst)
