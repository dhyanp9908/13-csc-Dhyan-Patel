import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime
import threading
import time





#color plette
COLORS = {
    'Baby_Blue': '#8babd4',
    'Black': '#000000',
}

class HomePage(tk.Frame):
    def __init__(self, parent):
         super().__init__(parent, bg=COLORS['Baby_Blue'])

         #Title
         title = tk.Label(self, text='Get It Done',
             font=('Cooper Hewitt', 64, 'bold'),
             bg=COLORS['#Baby_Blue'],
             fg=COLORS['Black'])
         title.pack(pady=(60,5))

window = tk.Tk()
window.geometry("1000x700")
window.configure(bg=COLORS['Baby_Blue'])

page = HomePage(window)
page.pack(fill='both', expand=True)

window.mainloop()#place window on computer screen, listen for events