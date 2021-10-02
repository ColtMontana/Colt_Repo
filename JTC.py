#This is a companion App to use while I'm on my JTC Zoom meetings

from tkinter import *
import webbrowser
import os
import subprocess
window=Tk()
window.geometry("200x300")
window.title("JTC Zoom Sessions")

new = 1
url = "https://courseworks2.columbia.edu/courses/141443/external_tools/24005"

url1 = "https://courseworks2.columbia.edu/courses/141443"

url2 = "https://www.google.com/"

url3 = "https://www.python.org/ftp/python/doc/quick-ref.1.3.html"


def openweb():
    webbrowser.open(url,new=new)

def openweb2():
    webbrowser.open(url1,new=new)

def openweb3():
    webbrowser.open(url2,new=new)

def openweb4():
    webbrowser.open(url3,new=new)

def myClick():
    myLabel = Label(window, text="JTC Zoom App")
    myLabel.pack()

def addApp():
    path = "/Applications/Slack.app"
    os.system(f"open {path}")

def addApp2():
    path = "/Applications/Spark.app"
    os.system(f"open {path}")


label1 = Label(window, text="JTC ZOOM CLASSES", fg="black", bg="orange", relief="solid",  font= ("arial", 18, "bold")).pack()

Btn = Button(text = "JTC Zoom", padx=10, pady=5, command=openweb)
Btn.pack()

Btn = Button(text = "Canvas", padx=10, pady=5, command=openweb2)
Btn.pack()

Btn3 = Button(text = "Slack", padx=10, pady=5, command=addApp)
Btn3.pack()

Btn4 = Button(text = "Spark", padx=10, pady=5, command=addApp2)
Btn4.pack()

Btn2 = Button(text = "Google", padx=10, pady=5, command=openweb3)
Btn2.pack()

Btn7 = Button(text = "Python Ref.", padx=10, pady=5, command=openweb4)
Btn7.pack()

myButton = Button(window, text="Info", padx=10, pady=5, command=myClick)
myButton.pack()

btn9 = Button(window, text="Quit", padx=10, pady=5, command=quit)
btn9.pack()

window.mainloop()

# Made by Colton McPhail using Visual Studio Code