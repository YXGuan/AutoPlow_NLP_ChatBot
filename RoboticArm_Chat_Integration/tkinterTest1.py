#!/usr/bin/python3
from tkinter import *
import subprocess

# a function to invode a bash script
def runSubprocess():
    subprocess.run(["./bashTest2.sh"])

root = Tk()
root.title('this is a title')
root.geometry("600x600")

#Define a function to close the window
def close_window():
   root.destroy()

# create the instances of two buttons
runSubprocessButton = Button(root, text= "Run SubProcess!", command=lambda: runSubprocess(),height = 10, width = 50)
closAllWindowsButton = Button(root, text= "close all windows (don't press this, use Control + C to exit!!!)", command=lambda: close_window(), height = 10, width = 50)

# add two buttons
runSubprocessButton.pack()
closAllWindowsButton.pack()

mainloop()