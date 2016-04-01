#simple GUI

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice here too
#create the windows

root = Tk()

#modify root window
root.title("Simple GUI")
root.geometry("200x100")

#kick off the event loop 
root.mainloop()

