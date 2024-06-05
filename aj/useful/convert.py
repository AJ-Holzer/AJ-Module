from typing import Any

def remove_duplicates(input_list: list[Any]):
    """Removes all duplicated items in a list and returns the formatted list."""
    return sorted(set(input_list))