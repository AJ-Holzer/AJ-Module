import os

def create_env(paths:list) -> None:
    """Creates the paths provided. (list)"""
    for path in list(paths):
        if not os.path.exists(path):
            os.makedirs(path)