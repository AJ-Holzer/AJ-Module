import customtkinter as tk

def yes_no_window(text: str, icon: str = "") -> bool:
    """
    Creates a ctk window with a yes/no question.
    
    :param text (str): The question to show on the window.
    :param icon (str): The icon to show on the window.
    :return (bool): The answer (yes: true, no: false).
    """
    # Use a local variable to store the result
    result: bool = False

    yesNoRoot: tk.CTk = tk.CTk()
    yesNoRoot.title("Yes/No Question")
    yesNoRoot.resizable(False, False)
    if icon:
        yesNoRoot.iconbitmap(icon)

    def yes() -> None:
        nonlocal result  # Use nonlocal to modify the variable in the enclosing scope
        result = True
        yesNoRoot.destroy()

    def no() -> None:
        nonlocal result  # Use nonlocal to modify the variable in the enclosing scope
        result = False
        yesNoRoot.destroy()

    label: tk.CTkLabel = tk.CTkLabel(yesNoRoot, text=text)
    label.pack(pady=10)

    yesButton: tk.CTkButton = tk.CTkButton(yesNoRoot, text="yes".upper(), command=yes)
    yesButton.pack(side="left", pady=10, padx=10)

    noButton: tk.CTkButton = tk.CTkButton(yesNoRoot, text="no".upper(), command=no)
    noButton.pack(side="right", pady=10, padx=10)

    yesNoRoot.mainloop()

    return result  # Return the result directly
