from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("500x500")
window.title("Get It Done")

window.config(background="#8babd4") #Background color

label = Label(window,
              text="Get It Done",
              font=('Cooper Hewitt',100, 'bold'),
              fg='#000000',
              bg='#8babd4')
label.pack(pady=(60,5))

import tkinter as tk

# black line
black_line = tk.Frame(window, bg=['#000000'], height=3, width=1000)
black_line.pack(pady=(0, 10))
black_line.pack_propagate(False)

def click():
    print ("hello")
button = Button(window, text=('Get Started')) #start button
button.config(command=click)
button.config(font=('Canva sans',60,'bold'))
button.config(bg='#ffffcc')
button.pack(pady=(200,25))



window.mainloop()#place window on computer screen, listen for events

