import os

def search_dir(dir: str, searchWord: str) -> list[tuple[str, int]]:
    """
    Searches for a word in a directory and its subdirectories.
    
    :param dir (str): The directory to search in.
    :param searchWord (str): The word to search for.
    :return (list[tuple[str, int]]): A list of tuples containing the file path and the line number where the word was
    """
    files: list[str] = [os.path.join(root, file) for root, _, files in os.walk(dir) for file in files]
    found: list[tuple[str, int]] = []

    for file in files:
        try:
            with open(file, "r", encoding="UTF-8") as f:
                for count, line in enumerate(f, 1):
                    if searchWord.lower() in line.lower():
                        found.append((file, count))
        except Exception:
            pass

    return found
