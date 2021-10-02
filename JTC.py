from tkinter import *
import webbrowser
window=Tk()
window.geometry("300x150")
window.title("JTC Zoom Sessions")

new = 1
url = "https://courseworks2.columbia.edu/courses/141443/external_tools/24005"



def openweb():
    webbrowser.open(url,new=new)

def myClick():
    myLabel = Label(window, text="This app launches JTC Zoom sessions page.")
    myLabel.pack()

    
label1 = Label(window, text="JTC ZOOM CLASSES", fg="black", bg="orange", relief="solid",  font= ("arial", 20, "bold")).pack()

Btn = Button(text = "JTC Zoom", padx=10, pady=5, command=openweb)
Btn.pack()

myButton = Button(window, text="Info", padx=10, pady=5, command=myClick)
myButton.pack()

window.mainloop()