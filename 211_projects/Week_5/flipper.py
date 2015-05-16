"""
flipper.py: CIS 211 assignment 4.3, Spring 2014
author: Ian Garrett, igarrett@uoregon.edu

displays three cards and rotates through them one at a time
"""

from tkinter import *
from random import randint
from CardLabel import *

sides = ['back', 'front', 'blank']
n = 0                          
side = 1

def flip():
    """
    flips card, tracks which card to flip with global variable n
    and the side to display with global variable side
    """
    global n, label
    global side, label

    index = randint(0,51)
    if n == 0:
    	label1.display(sides[side], index)
    if n == 1:
    	label2.display(sides[side], index)
    if n == 2:
    	label3.display(sides[side], index)
    	side += 1
    if side == 3:
    	side = 0

    n = (n + 1) % 3

root = Tk()

CardLabel.load_images()

label1 = CardLabel(root)
label1.grid(row=0, column=0)

label2 = CardLabel(root)
label2.grid(row=0, column=1)

label3 = CardLabel(root)
label3.grid(row=0, column=2)

root.rowconfigure(0, minsize=115)
root.columnconfigure(0, minsize=85)
root.columnconfigure(1, minsize=85)
root.columnconfigure(2, minsize=85)

button = Button(root, text='Flip', command=flip)
button.grid(row=1, column=1, pady = 10)

if __name__ == '__main__':
    root.mainloop()