class Settings:
    # Module settings here

    def __init__(self) -> None:
        self.send_init_msg: bool = True # If true --> The package will print, that it is initialized.
        self.ITALIC: str = "\033[3m"
        self.RESET: str = "\033[0m"
        self.green: str = "\033[92m"
        self.white: str = "\033[97m"

settings = Settings()