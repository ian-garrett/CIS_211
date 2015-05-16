# Simple app to test image labels.  

# CIS 211
# Spring 2014

# Note: see flip_one_frame.py for a better organization....

from tkinter import *
from random import randint
from CardLabel import *

sides = ['back', 'front', 'blank']  # values that can be passed to display method
n = 0                               # index into list of sides

def flip():
    global n, label
    n = (n + 1) % 3
    label.display(sides[n], randint(0,51))  # 2nd arg ignored if first is not 'front'

root = Tk()

CardLabel.load_images()             # call after creating top level app

label = CardLabel(root)             # image on a new CardLabel is 'back'
label.grid(row=0, column=0)         # call x.grid() to place widget x in its parent's grid

root.rowconfigure(0, minsize=115)   # note the grid is part of the parent...
root.columnconfigure(0, minsize=85)

button = Button(root, text='Flip', command=flip)
button.grid(row=1, column=0, pady = 10)

if __name__ == '__main__':
    root.mainloop()