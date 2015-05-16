"""
Card.py: CIS 211 assignment 2, Spring 2014
author: Ian Garrett, igarrett@uoregon.edu

Creates objects that represent cards given an int from 0 to 51. Other functions provide options for dealing with said objects.
"""
import sys

# part 1
class Card:
	'''
	A class representing a card

	Attributes:
		ID = int: identification

	Methods:
		rank(self): returns rank of Card object 
		suit(self): returns suit of Card object
		points(self): returns point value
	''' 
	def __init__(self,ID):
		self.ID = ID
		if not 0 <= self.ID <= 51: # extra credit
			raise ValueError("You must select a number between 0 and 51")

	def __repr__(self):
		rank_values = {9:'J',10:'Q',11:'K',12:'A'}
		symbols = {0:'\u2663',1:'\u2666',2:'\u2665',3:'\u2660'}
		if self.rank() <= 8:
			card_rank = (self.rank()+2)
		else:
			card_rank = rank_values[self.rank()]
		return (str(card_rank) + str(symbols[self.suit()]))

	def __lt__(self,other):
		return (self.ID < other.ID)

	def rank(self):
		#rank_values = {9:'J',10:'Q',11:'K',12:'A'}
		reduct_ID = self.ID
		while reduct_ID >= 13:
			reduct_ID -= 13
		return (reduct_ID)
		

	def suit(self):
		#symbols = {0:'\u2663',1:'\u2666',2:'\u2665',3:'\u2660'}
		if 0 <= self.ID <= 12:
			suit = 0
		elif 13 <= self.ID <= 25:
			suit = 1
		elif 26 <= self.ID <= 38:
			suit = 2
		else:
			suit = 3
		return suit

	def points(self):
		if self.rank() == 12:
			return 4
		elif self.rank() == 11:
			return 3
		elif self.rank() == 10:
			return 2
		elif self.rank() == 9:
			return 1
		return 0

# part 2
class BlackjackCard(Card):
	'''
	A class representing a Blackjack Card. Runs 
	through class Card for all methods with the 
	exception of points(), which is calculated
	using the method method within BlackjackCard

	Methods:
		points(self): returns point value
	'''
	def __lt__(self,other):
		return (self.rank() < other.rank())

	def points(self):
		face_cards = [11,10,9]
		if self.rank() == 12:
			return 11
		elif self.rank() in face_cards:
			return 10
		else:
			return (self.rank()+2)

# part 3
def points(self):
	'''
	Counts the number of points within a given hand

	Args:
		self = list: list of Card or BlackjackCard objects

	Returns:
		point_count = int: point count for list self
	'''
	face_cards = [11,10,9]
	point_count = 0
	for card in self:
		if card.rank() == 12:
			point_count += 11
		elif card.rank() in face_cards:
			point_count += 10
		else:
			point_count += (card.rank()+2)
	return point_count

# part 4 extra credit
def new_deck(module):
	'''
	Creates a new list of Card or BlackjackCard items

	Args:
		module = class: either Card or BlackjackCard, specifies 
						which Class items the list will containt

	Returns:
		new_deck = list: list of 52 Class items, either Card or BlackjackCard
	'''
	new_deck = []
	for i in range(52):
		new_deck.append(module(i))
	return (new_deck)
