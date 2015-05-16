"""
cleanup.py: CIS 211 assignment 8.1, Spring 2014
author: Ian Garrett, igarrett@uoregon.edu

deletes all temporary files from a directory
"""
import sys
from os import walk
from os import path
from os import remove

if len(sys.argv) < 2:
    raise Exception("enter a directory")
source = sys.argv[1]

temp_files = ['.aux', '.idx', '.ilg', '.ind', '.log', '.pdf', '.toc']

for directory in walk(source):
    for file in directory[2]:
        if path.splitext(file)[1] in temp_files:
            print(path.join(directory[0], file))
            remove(path.join(directory[0], file))