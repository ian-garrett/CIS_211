"""
backup.py: CIS 211 assignment 8.2, Spring 2014
author: Ian Garrett, igarrett@uoregon.edu

saves directory  to a new directory called 'versions', each call makes new subfolder within 'versions'
"""
import sys
from os import listdir
from os import mkdir
from os import path
from shutil import copytree

if len(sys.argv) < 2:
    raise Exception("enter a directory")
source = sys.argv[1]

if not path.isdir('versions'):
	mkdir('versions')
index = len(listdir('versions'))+1
if path.isdir('versions'):
	copytree(source,('versions/'+str(index)))