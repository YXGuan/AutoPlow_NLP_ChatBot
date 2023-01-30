#!/usr/bin/python3
import webbrowser
from tkinter import *
# TODO it's a bad idea to import * https://www.geeksforgeeks.org/why-import-star-in-python-is-a-bad-idea/
import subprocess


# TODO create logs, exception handling, log information and potential fix from Bash
# TODO UI UX redesign. create 3 groups  robot, arm, cam etc
# TODO add description to each button
# TODO upload to a seperate repo
# TODO log information not only in bash terminal but also in python program
# TODO a button to kill a PID
# TODO an actual log? to a file?
# TODO bash log with colour?

def runSubprocess():
    subprocess.run(["./bashTest2.sh"])

def armPicknPlace():
    subprocess.run(["./armPicknPlace.sh"])
def armPS4Controller():
    subprocess.run(["./armPS4Controller.sh"])
def armReplay():
    subprocess.run(["./armReplay.sh"])
def armPerception():
    subprocess.run(["./armPerception.sh"])
def armRecord():
    subprocess.run(["./armRecord.sh"])
def camCigButtDetection():
    subprocess.run(["./camCigButtDetection.sh"])
def camGeneralDetection():
    subprocess.run(["./camGeneralDetection.sh"])
def camGeneralDetectionWithDepth():
    subprocess.run(["./camGeneralDetectionWithDepth.sh"])
def chatbot():
    subprocess.run(["./chatbot.sh"])
    webbrowser.open('https://www.linkedin.com/feed/') 
def robotDocking():
    subprocess.run(["./robotDocking.sh"])
def robotHardCodedGoAndTurn():
    subprocess.run(["./robotHardCodedGoAndTurn.sh"])
def robotJoystick():
    subprocess.run(["./robotJoystick.sh"])
def robotRecordTrip1():
    subprocess.run(["./robotRecordTrip1.sh"])
def robotRecordTrip2():
    subprocess.run(["./robotRecordTrip2.sh"])
def robotReplayTrip1():
    subprocess.run(["./robotReplayTrip1.sh"])
def robotReplayTrip2():
    subprocess.run(["./robotReplayTrip2.sh"])
def robotTeleOp():
    subprocess.run(["./robotTeleOp.sh"])
def robotUnDock():
    subprocess.run(["./robotUnDock.sh"])
def robotWallFollwing():
    subprocess.run(["./robotWallFollwing.sh"])    

# def ():
#     subprocess.run(["./.sh"])

root = Tk()
root.title('this is a title')
root.geometry("1600x1600")

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


myButton = Button(root, height= 1, width=30, text= "click me!", command=lambda: clicked(r.get()))
myButton2 = Button(root, height= 1, width=30, text= "Run SubProcess!", command=lambda: runSubprocess())
myButton3 = Button(root, height= 1, width=30, text= "close all windows", command=lambda: close_win())
myButton4 = Button(root, height= 1, width=30, text= "armPicknPlace", command=lambda: armPicknPlace())
myButton5 = Button(root, height= 1, width=30, text= "armPS4Controller", command=lambda: armPS4Controller())
myButton6 = Button(root, height= 1, width=30, text= "armReplay", command=lambda: armReplay())
myButton61 = Button(root, height= 1, width=30, text= "armPerception", command=lambda: armPerception())
myButton62 = Button(root, height= 1, width=30, text= "armRecord", command=lambda: armRecord())
myButton7 = Button(root, height= 1, width=30, text= "camCigButtDetection", command=lambda: camCigButtDetection())
myButton8 = Button(root, height= 1, width=30, text= "camGeneralDetection", command=lambda: camGeneralDetection())
myButton9 = Button(root, height= 1, width=30, text= "camGeneralDetectionWithDepth", command=lambda: camGeneralDetectionWithDepth())
myButton10 = Button(root, height= 1, width=30, text= "chatbot", command=lambda: chatbot())
myButton11 = Button(root, height= 1, width=30, text= "robotDocking", command=lambda: robotDocking())
myButton12 = Button(root, height= 1, width=30, text= "robotHardCodedGoAndTurn", command=lambda: robotHardCodedGoAndTurn())
myButton13 = Button(root, height= 1, width=30, text= "robotJoystick", command=lambda: robotJoystick())
myButton14 = Button(root, height= 1, width=30, text= "robotRecordTrip1", command=lambda: robotRecordTrip1())
myButton15 = Button(root, height= 1, width=30, text= "robotRecordTrip2", command=lambda: robotRecordTrip2())
myButton16 = Button(root, height= 1, width=30, text= "robotReplayTrip1", command=lambda: robotReplayTrip1())
myButton17 = Button(root, height= 1, width=30, text= "robotReplayTrip2", command=lambda: robotReplayTrip2())
myButton18 = Button(root, height= 1, width=30, text= "robotTeleOp", command=lambda: robotTeleOp())
myButton19 = Button(root, height= 1, width=30, text= "robotUnDock", command=lambda: robotUnDock())
myButton20 = Button(root, height= 1, width=30, text= "robotWallFollwing", command=lambda: robotWallFollwing())





myLabel = Label(root, text=r.get())
myLabel.pack()

myButton.pack()
myButton2.pack()
myButton3.pack()
myButton4.pack()
myButton5.pack()
myButton6.pack()
myButton61.pack()
myButton62.pack()
myButton7.pack()
myButton8.pack()
myButton9.pack()
myButton10.pack()
myButton11.pack()
myButton12.pack()
myButton13.pack()
myButton14.pack()
myButton15.pack()
myButton16.pack()
myButton17.pack()
myButton18.pack()
myButton19.pack()
myButton20.pack()





mainloop()



# .pack() --> Pack a widget in the parent widget.

# vertical = Scale(root, from_=0, to=200)
# vertical.pack()

# horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
# horizontal.pack()

# my_label = Label(root, text=horizontal.get()).pack()

# def slide():
#     my_label = Label