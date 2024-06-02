import os, sys, shutil

def get_python_version():
    version = sys.version.replace(".", "")[:3:]
    return version

def install():
    destination = f"C:/Users/{os.getenv("username")}/AppData/Local/Programs/Python/Python{get_python_version()}/Lib/site-packages"
    print(destination)

    items = []

    for dirpath, _, dirfile in os.walk("aj"):
        for dirfile in dirfile:
            items.append(os.path.join(str(dirpath), str(dirfile)))

    for file in items:
        target_file = os.path.join(destination, file)

        if not os.path.exists(os.path.dirname(target_file)):
            os.makedirs(os.path.dirname(target_file))

        if not os.path.exists(target_file):
            print(f"Creating file: {str(target_file)}")
        else:
            print(f"Updating file: {str(target_file)}")

        with open(file, "rb") as f:
            tmp = f.read()

            with open(target_file, "wb") as f:
                f.write(tmp)

def cleanup(root_dir: str) -> None:
    """
    Recursively removes all __pycache__ subdirectories in the given root directory.
    
    Parameters:
        root_dir (str): The root directory to start the search from.
    """
    for dirpath, dirnames, _ in os.walk(root_dir):
        if "__pycache__" in dirnames:
            pycache_dir = os.path.join(dirpath, "__pycache__")
            try:
                shutil.rmtree(pycache_dir)
                print(f"Removed: {pycache_dir}")
            except Exception as e:
                print(f"Failed to remove {pycache_dir}: {e}")

def main():
    cleanup(root_dir="aj")
    install()

if __name__ == "__main__":
    main()