import os

files: dict[str, str] = {
    "main.py": """import ajpack

def main() -> None:
    ...

if __name__ == "__main__": main()

""",
    "env/func/Classes.py": ""
}

def build_environment() -> None:
    """Creates a new main.py file with an env folder and a lot other stuff for a new project."""
    for file, content in files.items():
        dirname: str = os.path.dirname(file)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        with open(file, "w", encoding="UTF-8") as f:
            f.write(content)
