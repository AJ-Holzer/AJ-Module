class Settings:
    # Module settings here

    def __init__(self) -> None:
        self.send_init_msg: bool = True
        self.ITALIC: str = "\033[3m"
        self.RESET: str = "\033[0m"

settings = Settings()