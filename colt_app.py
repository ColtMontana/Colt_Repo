from tkinter import *
import webbrowser
window=Tk()
window.geometry("300x200")
window.title("COLT BKMT")

new = 1
url = "https://coltnyc.tumblr.com/"

new = 2
url2 = "https://www.youtube.com/watch?v=aUYt0UYYFJQ"

myname = "Colt Montana"
mymail = "cwmcphail90@gmail.com"



def full_name():
    print(myname)
    print(mymail)


def openweb():
    webbrowser.open(url,new=new)

def openweb2():
    webbrowser.open(url2,new=new)

def myClick():
    myLabel = Label(window, text="Colt Montana \n cwmcphail@gmail.com")
    myLabel.pack()

    
label1 = Label(window, text="The Official App of Colt Montana", fg="black", bg="red", relief="solid",  font= ("arial", 18, "bold")).pack()

Btn = Button(text = "Music", padx=10, pady=5, command=openweb)
Btn.pack()

button3 = Button(text="Country Boy Mile High Video", padx=10, pady=5, command=openweb2)
button3.pack()


myButton = Button(window, text="Info", padx=10, pady=5, command=myClick)
myButton.pack()

quit_button = Button(window, text="Quit", padx=10, pady=5, command=quit)
quit_button.pack()

window.mainloop()