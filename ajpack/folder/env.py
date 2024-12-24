import os

def _create_paths(paths: list[str]) -> None:
    """Create directories if they do not exist."""
    for path in paths:
        try:
            os.makedirs(path, exist_ok=True)
        except Exception as e:
            raise Exception(f"There was an exception while creating the path '{path}'! --> {e}")

def create_env(paths: list[str]) -> None:
    """
    Creates the paths provided. (list)
    
    :param paths (list[str]): The paths to create.
    """
    _create_paths(paths)

def create_standard_env() -> None:
    """
    Creates the standard paths for the project.
    (env, env/logs, env/data, env/images, env/func)
    """
    paths = [
        "env",
        "env/logs",
        "env/data",
        "env/images",
        "env/func",
    ]

    _create_paths(paths)
