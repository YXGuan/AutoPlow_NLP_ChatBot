#!/usr/bin/python3

from tkinter import *
import subprocess


def runSubprocess():
    subprocess.run(["./bashTest2.sh"])
    # subprocess.run(["ls", "-l"])
    # ./home/yuxiang/code/2023/AutoPlow_NLP_ChatBot/VoiceEnabled_RoboticArmPicking/bashTest2.sh


root = Tk()
root.title('this is a title')
root.geometry("600x600")

r = IntVar()
r.set("2")

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

#Define a function to close the window
def close_win():
   root.destroy()

Radiobutton(root, text="Option 1", variable = r, value=1,command=lambda:clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable = r, value=2,command=lambda:clicked(r.get())).pack()

myLabel = Label(root, text=r.get())
myLabel.pack()

myButton = Button(root, text= "click me!", command=lambda: clicked(r.get()))
myButton2 = Button(root, text= "Run SubProcess!", command=lambda: runSubprocess())
myButton3 = Button(root, text= "close all windows", command=lambda: close_win())

myButton.pack()
myButton2.pack()
myButton3.pack()


mainloop()



# .pack() --> Pack a widget in the parent widget.

# vertical = Scale(root, from_=0, to=200)
# vertical.pack()

# horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
# horizontal.pack()

# my_label = Label(root, text=horizontal.get()).pack()

# def slide():
#     my_label = Label