class Settings:
    # Module settings here
    def __init__(self) -> None:
        # INIT settings
        self.send_init_msg: bool = True          # If true --> The package will print, that it is initialized.

        # Formats
        self.BOLD: str = "\033[1m"               # Format bold
        self.ITALIC: str = "\033[3m"             # Format italic
        self.UNDERLINE: str = "\033[4m"          # Format underline
        self.INVISIBLE: str = "\033[8m"          # Format invisible
        self.STRIKETHROUGH: str = "\033[9m"      # Format strike through
        self.UNDERLINE_DOUBLE: str = "\033[21m"  # Format double underline

        # Colors
        self.RESET: str = "\033[0m"              # Reset color
        self.GRAY: str = "\033[90m"              # Gray
        self.RED: str = "\033[91m"               # Red
        self.GREEN: str = "\033[92m"             # Green
        self.YELLOW: str = "\033[93m"            # Yellow
        self.BLUE: str = "\033[94m"              # Blue
        self.MAGENTA: str = "\033[95m"           # Magenta
        self.CYAN: str = "\033[96m"              # Cyan
        self.WHITE: str = "\033[97m"             # White

settings = Settings()
 
# Indicator, that code is missing
def code_missing() -> None:
    # Raise error
    raise NotImplementedError("Sry, code is missing... Please contact me on the discord channel. (https://discord.gg/HvwFgC54UJ)")