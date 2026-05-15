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

button = tkinter.Button(window, text='Get Started', command=window. )



window.mainloop()#place window on computer screen, listen for events

