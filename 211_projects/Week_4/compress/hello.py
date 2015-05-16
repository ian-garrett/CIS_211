"""
hello.py: CIS 211 assignment 4.1, Spring 2014
author: Ian Garrett, igarrett@uoregon.edu

prints 'Hello, world' in a GUI box
"""

from tkinter import * 

root = Tk()

hello = Label(master = root, text = 'Hello, world')
hello.pack()

root.mainloop()
