import customtkinter as tk # type:ignore

def center_ctk(WINDOW: tk.CTk, width: int, height: int) -> None:
    """
    Centers the window on the screen.
    
    :param WINDOW (ctk.CTk): Window to center.
    :param width (int): Width of the window.
    :param height (int): Height of the window.
    :return (None):
    """
    WINDOW.update_idletasks()

    screenWidth = WINDOW.winfo_screenwidth()
    screenHeight = WINDOW.winfo_screenheight()

    x = (screenWidth // 2) - (width // 2)
    y = (screenHeight // 2) - (height // 2)

    WINDOW.geometry(f"{width}x{height}+{x}+{y}")
