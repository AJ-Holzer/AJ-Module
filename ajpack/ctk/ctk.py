import customtkinter as tk # type:ignore

def center_ctk(PARENT: tk.CTk) -> None:
    """Centers the window on the screen."""
    PARENT.update_idletasks()
    width = PARENT.winfo_width()
    height = PARENT.winfo_height()

    screen_width = PARENT.winfo_screenwidth()
    screen_height = PARENT.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    PARENT.geometry(f"{width}x{height}+{x}+{y}")