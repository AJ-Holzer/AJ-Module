import customtkinter as tk

def yes_no_window(text: str, icon: str|None = None) -> bool:
    """Creates a window with a yes/no question and returns the answer as a boolean"""
    global state

    yes_no_root: tk.CTk = tk.CTk()
    yes_no_root.title("Yes/No Question")
    yes_no_root.geometry("300x100")
    yes_no_root.resizable(False, False)
    if icon: yes_no_root.iconbitmap(icon)

    state = False

    def yes() -> bool: global state; yes_no_root.destroy(); state = True
    def no() -> bool:  global state; yes_no_root.destroy(); state = False

    label: tk.CTkLabel = tk.CTkLabel(yes_no_root, text=text)
    label.pack(pady=10)

    yes_button: tk.CTkButton = tk.CTkButton(yes_no_root, text="yes".upper(), command=lambda: yes())
    yes_button.pack(side="left", pady=10, padx = 10)

    no_button: tk.CTkButton = tk.CTkButton(yes_no_root, text="no".upper(), command=lambda: no())
    no_button.pack(side="right", pady=10, padx=10)

    yes_no_root.mainloop()

    return state == True