import sys, os

def get_base_path() -> str:
    """Get the base path for the project."""
    if hasattr(sys, '_MEIPASS'):
        # Running in a PyInstaller bundle
        return sys._MEIPASS
    else:
        # Running in a normal Python environment
        return os.path.abspath(".")