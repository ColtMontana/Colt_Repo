from tkinter import *
import webbrowser

root = Tk()

root.geometry("100x50")

new = 1
url = "https://www.gmail.com"

def openweb():
    webbrowser.open(url,new=new)

Btn = Button(root, text = "GMAIL!",command=openweb)
Btn.pack()

root.mainloop()