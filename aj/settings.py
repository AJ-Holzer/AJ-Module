class Settings:
    # Module settings here

    def __init__(self) -> None:
        self.send_init_msg = True
        self.ITALIC = "\033[3m"
        self.RESET = "\033[0m"

settings = Settings()