"""
print_names.py: CIS 211 assignment 1.2, Spring 2014
author: Ian Garrett, igarrett@uoregon.edu

Reads a set of names from a text file into a list, sorts that list by either first or last name, and 
prints said list, one name per line. If sys.argv[3] is given as 'inits', first names are printed as first initials.
"""
import sys

class Name:
	'''
	A class representing a name.

	Attributes:
		first = str: first name
		last = str: last name

	Methods:
		first(self): returns first name
		last(self): returns last name)
    '''
	def __init__(self, first, last):
		self.first = first
		self.last = last

	def first(self):
		return self.first

	def last(self):
		return self.last

def name_list(text_file):
	'''
	reads text file containing 1 name per line and creates and stores a Name object for each name

	Args:
		text_file = .txt: text file containing list of names

	Returns:
		names = list: a list of Name objects
	'''
	with open(text_file) as f:
		name_text = f.read().splitlines()
	names = []
	for name in name_text:
		first = name.split()[0]
		last = name.split()[1]
		x = Name(first, last)
		names.append(x)
	return names

def print_names(name_list, sort_order, abrev = 'stop'):
	'''
	prints list of names sorted by either first or last name.
	additional arg abrev allows for the print method to be modified
	so that the first name is replaced with only its first initial

	Args:
		name_list = list: list of names, provided by name_list function
		sort_order = str: either 'first' or 'last', specifies how names are sorted
		abrev = str: optional variable, if user enters 'inits' for abrev, first names become their initial

	Returns:
		nothing

	Effects:
		prints sorted list of names
	'''
	if sort_order == 'first':
		name_list.sort(key = Name.first)
		if abrev == 'inits':
			for name in name_list:
				print (Name.first(name)[0] + '. ' + (Name.last(name)))
		else:
			for name in name_list:
				print (Name.first(name), Name.last(name))
	else:
		name_list.sort(key = Name.last)
		if abrev == 'inits':
			for name in name_list:
				print (Name.last(name) + ', ' + (Name.first(name))[0] + '.')
		else:
			for name in name_list:
				print (Name.last(name) + ', ' + Name.first(name))

final_list = name_list(sys.argv[1])

if len(sys.argv) > 3:
	print_names(final_list, sys.argv[2], sys.argv[3])
else:
	print_names(final_list, sys.argv[2])