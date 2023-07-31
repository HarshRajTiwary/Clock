from tkinter import *
import time

def ut():
    ct = time.strftime("%H:%M:%S")
    c.config(text=ct)
    c.after(1000, ut)

root = Tk()
root.title("Digital Clock")

c = Label(root, font=("Arial", 80))
c.pack(padx=50, pady=50)

ut()

root.mainloop()
