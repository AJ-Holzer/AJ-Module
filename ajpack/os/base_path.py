import sys, os

def get_base_path() -> str:
    """
    Get the base path for the project.
    
    :return (str): The base path of the project.
    """    
    return sys._MEIPASS if hasattr(sys, "_MEIPASS") else os.path.abspath(".")
