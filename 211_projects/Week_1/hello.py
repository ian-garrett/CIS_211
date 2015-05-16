"""
hello.py: CIS 211 assignment 1.1, Spring 2014
author: Ian Garrett, igarrett@uoregon.edu

Prints 'hello, world' in 1 of 4 languages. By default, the language is set as english.
If the language given is not a key within dictionary lang_dict, program prints an apology 
explaining that the language asked for is not known by the program.
"""
import sys

lang_dict = {'english': 'Hello, world', 'french': 'Bounjour tout le monde', 'spanish': 'Hola, mundo', 'german': 'Hallo, welt'}

def hello(lang = 'english'):
	'''
	Prints "Hello world" in 1 of 4 languages (english, french, spanish, german)

	Args:
		lang = str: optional arg provided by user. Specifies which language to user

	Returns:
		nothing

	Effects:
		prints 'hello world' in specified language, or explains to user that the language they asked for is not known
	'''
	if (lang in lang_dict):
		print (lang_dict.get(lang))
	else:
		print ("Sorry, I don't speak", lang.title())

if len(sys.argv) > 1:
	lang = str(sys.argv[1])
	hello(lang)
else:
	hello()