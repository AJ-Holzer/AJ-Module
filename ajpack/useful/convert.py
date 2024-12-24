import ast
from typing import Any

def remove_duplicates(input_list: list[Any]) -> list[Any]:
    """
    Removes all duplicated items in a list and returns the formatted list.

    :param input_list: The list to use.
    :return: The list without the doubled elements.
    """
    return sorted(set(input_list))

def str_to_dict(input_str: str) -> dict[Any, Any]:
    """
    Converts a string to a dictionary.
    
    :param input_str: String to convert.
    :return: String as a dictionary.
    """
    return ast.literal_eval(input_str)
