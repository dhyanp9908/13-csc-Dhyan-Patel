import tkinter as tk
from tkinter import ttk, messagebox
import datetime


BG = "#7B8FBF"  # blue background
CARD = "#F5F0C8"  # cream for buttons / cards
DARK = "#1A1A2E"  # dark text
SIDEBAR = "#F5F0C8"


T_TITLE = ("Georgia", 36, "bold")
T_SUB = ("Georgia", 16, "bold")
T_BODY = ("Georgia", 13)
T_BTN = ("Georgia", 14, "bold")
T_SM = ("Georgia", 11)



def btn(parent, label, action, w=12):
   return tk.Button(parent, text=label, command=action,
                    font=T_BTN, bg=CARD, fg=DARK,
                    relief="flat", padx=16, pady=8,
                    width=w, cursor="hand2",
                    activebackground="#E8E2AA")


class Page1(tk.Frame):
   def __init__(self, master, go_to_page2):
       super().__init__(master, bg=BG)


       # title + line
       tk.Label(self, text="Get It Done", font=T_TITLE, bg=BG, fg=DARK).pack(pady=(20, 4))
       tk.Frame(self, bg=DARK, height=2, width=500).pack()


       # quotes
       tk.Label(self, text="Stay Organized, Stay Creative.",
                font=T_SUB, bg=BG, fg=DARK).pack(pady=(20, 14))



       btn(self, "Get started", go_to_page2, w=16).pack()


       tk.Label(self, text="Never give up",
                font=("Georgia", 20, "bold"), bg=BG, fg=DARK).pack(pady=26)


       # bottom
       bot = tk.Frame(self, bg=BG)
       bot.pack(fill="x", padx=30, side="bottom", pady=16)
       tk.Label(bot, text="📝✅", font=("Arial", 26), bg=BG).pack(side="left")
       btn(bot, "Next", go_to_page2, w=8).pack(side="right")




#page 2 sigh in
class Page2(tk.Frame):
   def __init__(self, master, go_to_page1, go_to_page3):
       super().__init__(master, bg=BG)
       self._go3 = go_to_page3


       # icons row
       top = tk.Frame(self, bg=BG)
       top.pack(fill="x", padx=30, pady=(24, 0))
       tk.Label(top, text="📋✏️", font=("Arial", 26), bg=BG).pack(side="left")
       tk.Label(top, text="you can\ndo it",
                font=("Courier", 12, "bold"), bg="white", fg=DARK,
                padx=8, pady=4).pack(side="right")


       # title
       tk.Label(self, text="Get It Done", font=T_TITLE, bg=BG, fg=DARK).pack(pady=(12, 2))
       tk.Label(self, text="Stay on track",
                font=("Georgia", 20, "bold"), bg=BG, fg=DARK).pack()


       # name field
       tk.Label(self, text="Please enter your name to proceed",
                font=T_BODY, bg=BG, fg=DARK).pack(pady=(20, 6))
       name_frm = tk.Frame(self, bg=CARD, padx=14, pady=8)
       name_frm.pack()
       tk.Label(name_frm, text="Name:", font=("Georgia", 12, "bold"),
                bg=CARD, fg=DARK).pack(side="left", padx=(0, 8))
       self.name_var = tk.StringVar()
       tk.Entry(name_frm, textvariable=self.name_var,
                font=T_BODY, bg=CARD, relief="flat", width=22,
                insertbackground=DARK).pack(side="left")


       # student type
       tk.Label(self, text="What type of student are you?",
                font=T_BODY, bg=BG, fg=DARK).pack(pady=(16, 6))
       sel_frm = tk.Frame(self, bg=CARD, padx=14, pady=8)
       sel_frm.pack()
       tk.Label(sel_frm, text="Select:", font=("Georgia", 13, "bold"),
                bg=CARD, fg=DARK).pack(side="left", padx=(0, 12))
       self.type_var = tk.StringVar(value="High school student")
       ttk.Combobox(sel_frm, textvariable=self.type_var, state="readonly",
                    values=["High school student", "University student"],
                    font=T_BODY, width=22).pack(side="left")


       # quotes
       tk.Label(self, text='"Closer to your goal than yesterday"',
                font=("Georgia", 13, "italic"), bg=BG, fg=DARK).pack(pady=(18, 2))
       tk.Label(self, text="Do it for you",
                font=("Georgia", 15), bg=BG, fg=DARK).pack()

       # nav buttons
       nav = tk.Frame(self, bg=BG)
       nav.pack(fill="x", padx=30, side="bottom", pady=20)
       btn(nav, "Back", go_to_page1, w=8).pack(side="left")
       # NEXT button validates then goes to page 3
       btn(nav, "Next", self._next_clicked, w=8).pack(side="right")


   def _next_clicked(self):
       name = self.name_var.get().strip()
       if not name:
           messagebox.showwarning("Name required", "Please enter your name first.")
           return
       # pass name + student type to page 3
       self._go3(name, self.type_var.get())

#page 3
class Page3(tk.Frame):
   def __init__(self, master, go_to_page2, user_name, student_type):
       super().__init__(master, bg=BG)
       self.user_name = user_name
       self.student_type = student_type
       self.tasks = []
       self._build()


   def _build(self):
       outer = tk.Frame(self, bg=BG)
       outer.pack(fill="both", expand=True)


       # sidebar
       side = tk.Frame(outer, bg=SIDEBAR, width=170)
       side.pack(side="left", fill="y")
       side.pack_propagate(False)
       tk.Label(side, text="Calendar", font=("Georgia", 14, "bold"), bg=SIDEBAR, fg=DARK).pack(pady=(40, 6))
       tk.Label(side, text="Today's Work", font=T_SM, bg=SIDEBAR, fg=DARK).pack()
       tk.Label(side, text="Next 7\ndays work", font=("Georgia", 13, "bold"), bg=SIDEBAR, fg=DARK).pack(pady=(8, 0))
       tk.Label(side, text="🎯", font=("Arial", 46), bg=SIDEBAR).pack(side="bottom", pady=24)


       # main area
       main = tk.Frame(outer, bg=BG)
       main.pack(side="left", fill="both", expand=True, padx=18, pady=16)


       tk.Label(main, text=f"Hello, {self.user_name}!  ({self.student_type})",
                font=T_SM, bg=BG, fg=DARK).pack(anchor="e")
       tk.Label(main, text="To do list", font=("Georgia", 26, "bold"), bg=BG, fg=DARK).pack()
       tk.Frame(main, bg=DARK, height=2, width=440).pack(pady=(2, 10))


       # input row
       inp = tk.Frame(main, bg=BG)
       inp.pack(fill="x", pady=(0, 8))
       tk.Label(inp, text="Task:", font=("Georgia", 11, "bold"), bg=BG, fg=DARK).grid(row=0, column=0, padx=(0, 4))
       self.task_var = tk.StringVar()
       tk.Entry(inp, textvariable=self.task_var, font=T_BODY, bg=CARD, relief="flat", width=24,
                insertbackground=DARK).grid(row=0, column=1, padx=4)
       tk.Label(inp, text="Priority:", font=("Georgia", 11, "bold"), bg=BG, fg=DARK).grid(row=0, column=2, padx=(8, 4))
       self.prio_var = tk.StringVar(value="Medium")
       ttk.Combobox(inp, textvariable=self.prio_var, values=["High", "Medium", "Low"],
                    state="readonly", font=T_SM, width=9).grid(row=0, column=3, padx=4)
       tk.Label(inp, text="Due:", font=("Georgia", 11, "bold"), bg=BG, fg=DARK).grid(row=0, column=4, padx=(8, 4))
       self.due_var = tk.StringVar(value=datetime.date.today().strftime("%d/%m/%y"))
       tk.Entry(inp, textvariable=self.due_var, font=T_BODY, bg=CARD, relief="flat", width=9,
                insertbackground=DARK).grid(row=0, column=5, padx=4)
       btn(inp, "Add", self._add, w=5).grid(row=0, column=6, padx=(8, 0))


       # three columns
       cols = tk.Frame(main, bg=BG)
       cols.pack(fill="both", expand=True)


       df = tk.Frame(cols, bg=BG, width=130)
       df.pack(side="left", fill="y", padx=(0, 8))
       tk.Label(df, text="Do first", font=("Georgia", 12, "bold"), bg=BG, fg=DARK).pack()
       tk.Frame(df, bg=DARK, height=2, width=120).pack(pady=2)
       self.df_frame = tk.Frame(df, bg=BG);
       self.df_frame.pack(fill="both", expand=True)


       mid = tk.Frame(cols, bg=BG)
       mid.pack(side="left", fill="both", expand=True)
       self.mid_frame = tk.Frame(mid, bg=BG);
       self.mid_frame.pack(fill="both", expand=True)


       pr = tk.Frame(cols, bg=BG, width=155)
       pr.pack(side="right", fill="y", padx=(8, 0))
       tk.Label(pr, text="Priorities", font=("Georgia", 12, "bold"), bg=BG, fg=DARK).pack()
       tk.Frame(pr, bg=DARK, height=2, width=145).pack(pady=2)
       self.pr_frame = tk.Frame(pr, bg=BG);
       self.pr_frame.pack(fill="both", expand=True)
       tk.Label(pr, text="Due dates", font=T_SM, bg=BG, fg=DARK).pack(pady=(8, 2))
       tk.Label(pr, text="📅", font=("Arial", 26), bg=BG).pack()


       # bottom bar
       bot = tk.Frame(main, bg=BG)
       bot.pack(fill="x", pady=(10, 0))
       btn(bot, "Save", self._save, w=7).pack(side="left", padx=(0, 6))
       btn(bot, "Back", lambda: self.master.master._show_page2_back(), w=7).pack(side="left")
       tk.Label(bot, text="Just do it", font=("Georgia", 13, "bold"), bg=BG, fg=DARK).pack(side="left", expand=True)
       btn(bot, "Done", self._done_check, w=7).pack(side="right")

def _add(self):
    text = self.task_var.get().strip
    if not text:
        messagebox.showwarning("Empty","Please type a task first")
        return
    self.tasks.append({"text": text, "prio": self. prio_var.get(),
                       "due": self.due_var.get(), "done": False,
                       "var": tk.BooleanVar()})
    self.task_var.set("")
    self._refresh()

def _refresh(self):
    for f in (self.df_frame, self.mid_frame, self.pr_frame):
        for w in f.winfo_children() : w.destroy()

    for t in slef.task:
        clr = {"High": "#C0392B", "Medium": DARK, "Low": "#2C7A3A"} [t["prio"]
        #priorities sidebar
        tk.Label(self.pr_frame, text=f"o {t['text'] [:15]}", font=T_SM, bg=BG, fg =clr) .pack(anchor="w")
        #do-first or main list
        if t["prio"] == "High":
            self._row(self.df_frame, t)
        else:
            self._row(self.mid_frame, t)

def _row(self, parent, task):





class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Get It Done")
        self.geometry("900x600")
        self.configure(bg=BG)





if __name__ == "__main__":
    App().mainloop()



