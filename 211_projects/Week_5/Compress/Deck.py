"""
Deck.py: CIS 211 assignment 3, Spring 2014
author: Ian Garrett, igarrett@uoregon.edu

Creates lists of Card objects to simulate 51 card decks or 48 card decks
"""


import random

from Card import *

class Deck(list):
	'''
	Class that builds a 51 card deck out of Card objects

	Args:
		List: Allows list methods to be called in class functions

	Methods:
		shuffle(self): Shuffles Deck object
		deal(self, n): Takes n number of cards from Deck object and returns
			           them in a list
		restore(self, a): Runs through list a and adds them back into Deck object

	'''
	def __init__(self):
		# extra credit, checks that type of object is a Card object
		for i in range(52):
			if isinstance(Card(i), Card):
				self.append(Card(i))
			else:
				print (Card(i),"is not a Card object")

		#self.append[cls(i) for i in range(52)]

	def shuffle(self):
		random.shuffle(self)

	def deal(self, n, hands = 1):
		# extra credit deal, deals multiple hands of length n
		all_hands = []
		if hands == 1:
			hand = []
			for card in range(n):
				hand.append(self.pop())
			return hand
		for hand in range(hands):
			hand = []
			for card in range(n):
				hand.append(self.pop())
			all_hands.append(hand)
		return all_hands

	def nextcard(self):
		'''
		pop and returns last Card object from self

		args:
			self = list: list of Card objects

		returns:
			self.pop() = Card object: top card from self
		'''
		return (self.pop())

	def restore(self, hands):
		# extra credit restore, verifies that objects being appended to self are Card objects
		if isinstance(hands[0], Card):
			for card in hands:
				if isinstance(card, Card):
					self.append(card)
				else:
					print (card,"is not a Card object")
		else:
			for hand in hands:
				for card in hand:
					if isinstance(card, Card):
						self.append(card)
					else:
						print (card,"is not a Card object")

class PinochleDeck(Deck):
	'''
	A subclass of Deck, contains only cards rank 9-A, adds each card twice
	'''
	def __init__(self):
		not_cards = [0,1,2,3,4,5,6]
		for i in range(52):
			if Card(i).rank() in not_cards:
				continue
			else:
				self.append(Card(i))
				self.append(Card(i))
