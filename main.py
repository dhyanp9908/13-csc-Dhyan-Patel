import tkinter as tk
from tkinter import ttk, messagebox
import datetime




BG = "#8babd4"
CARD = "#ffffcc"
DARK = "#000000"
SIDEBAR = "#F5F0c8"

T_TITLE = ("Georgia", 36, "bold")
T_SUB = ("Georgia", 16, "bold")
T_BODY = ("Georgia", 13)
T_BTN = ("Georgia", 14, "bold")
T_SM = ("Georgia", 11)



def btn(parent, label, action, w:int=12):
    return tk.Button(parent, text=label, command=action,
                     font=T_BTN, bg=CARD, fg=DARK,
                     relief="flat", padx=16, pady=8,
                     width=w, cursor="hand2",
                     activebackground="#E8E2AA")
class Page1(tk.Frame):
    def __init__(self, master:Misc|None, go_to_page2):
        super().__init__(master, bg=BG)

    tk.Label(self, text="Get It Done", font=T_TITLE, bg=BG, fg=DARK).pack(pady=(20, 4))
    tk.Frame(self, bg=DARK, height =2, width=500).pack()

    tk.Label(self, text="Stay Organized, Stay Creative",
             font=T_SUB, bg=BG, fg=DARK). pack(pady=(20,14))

    btn(self, "Get Started")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Get It Done")
        self.geometry("900x600")
        self.configure(bg=BG)









if __name__ == "__main__":
    App().mainloop()



