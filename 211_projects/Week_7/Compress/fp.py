"""
fp.py: CIS 211 assignment 7, Spring 2014
author: Ian Garrett, igarrett@uoregon.edu

a collection of five functions that utilize functional programming
"""

#1
def codes(x):
	return list(map(ord, x))

#2 
def vowels(x):
	vowels = ['a','e','i','o','u','A','E','I','O','U']
	go_do = lambda t: t if t in vowels else ""
	return "".join(list(map(go_do, list(x))))

#3 
def tokens(x):
	from string import punctuation
	strip = lambda t: t.strip(punctuation)
	return map(strip, x.split())

#4
def numbers(x):
	return list(filter(str.isdigit,list(tokens(x))))

#5
def sq_ft(x):
	class Room:
		def __init__(self, Entry):
			self.name,self.width,self.depth = Entry.split()
		def area(self):
			return float(int(self.width)*int(self.depth))
	from operator import add
	from functools import reduce
	calc_room = lambda t: (Room(t)).area()
	return reduce(add,list(map(calc_room, open(x))))

print (sq_ft("house.txt"))
