"""
blackjack.py: CIS 211 assignment 5, Spring 2014
author: Ian Garrett, igarrett@uoregon.edu

a fully functional blackjack game
"""
from tkinter import *
from tkinter.messagebox import showinfo
from CardLabel import *
from Deck import *

root = Tk()

CardLabel.load_images()

dealer_hand_display = []
player_hand_display = []

dealer_hand = []
player_hand = []
global_deck = Deck()

# extra credit, tracks wins of player and dealer
dealerwin_count = 0
playerwin_count = 0

def process_bet(winner):
	'''
	calculates and displays new account balance (extra credit)

	args:
		winner = string: either 'player' or 'dealer'
	'''
	if len(bet.get()) > 0:
		balance_x = float(bet.get())
	if len(current_bet.get()) > 0:
		bet_x = float(current_bet.get())
		if winner == 'player':
			new_balance = (balance_x+bet_x)
		if winner == 'dealer':
			new_balance = (balance_x-bet_x)
		bet.config(state=NORMAL)
		bet.delete(0,END)
		bet.insert(0,('%.2f' % new_balance))
		bet.config(state=DISABLED)
		current_bet.delete(0,END)

def total(hand):
	'''
	totals the number of points in any given hand of cards

	args:
		hand = list: list of Card objects
	'''
	aces = 0
	total = 0
	face_cards = [9,10,11]
	for card in hand:
		if card.rank() in face_cards:
			total += 10
		elif card.rank() == 12:
			total += 11
			aces += 1
		else:
			total += (card.rank()+2)
	while (total > 21) and (aces > 0):
		total -= 10
		aces -= 1
	return total

def win_process(winner):
	'''
	announces winner and updates scoreboard (extra credit) and bet balance (exra credit)

	args:
		winner = string: 'players' or 'dealer'

	effect:
		brings up window informing player who won
		updates scoreboard
	'''
	global dealerwin_count
	global playerwin_count

	dealer_hand_display[0].display('front', dealer_hand[0].ID)
	if winner == 'player':
		showinfo("Game over", "You win!")
		playerwin_count += 1
		player_wins.config(state=NORMAL)
		player_wins.delete(0,END)
		player_wins.insert(0,str(playerwin_count))
		player_wins.config(state=DISABLED)
	if winner == 'dealer':
		showinfo("Game over", "Dealer wins...")
		dealerwin_count += 1
		dealer_wins.config(state=NORMAL)
		dealer_wins.delete(0,END)
		dealer_wins.insert(0,str(dealerwin_count))
		dealer_wins.config(state=DISABLED)

	# extra credit, processes bet
	process_bet(winner)

def display_row(contestant):
	'''
	displays 6 cards in a row

	args:
		contestant = string: specifies which row cards are the be displayed on
	
	effect:

	'''
	global dealer_hand_display
	global player_hand_display

	if contestant == 'player':
		vs = 1
		save_loc = player_hand_display
	if contestant == 'dealer':
		vs = 0
		save_loc = dealer_hand_display
	for i in range(6):
		card_disp = CardLabel(root)
		card_disp.grid(row=vs,column=(i))
		root.columnconfigure(i, minsize=85)
		save_loc.append(card_disp)
		card_disp.display('blank')

def deal():
	'''
	resets game, deals 4 cards face down, flips 3 to begin (1 dealer, 2 player)
	'''
	global dealer_hand_display
	global player_hand_display

	global dealer_hand
	global player_hand
	global global_deck

	# resets global variables and shuffles deck, creating new game
	dealer_hand = []
	player_hand = []
	global_deck = Deck()
	global_deck.shuffle()

	current_bet.config(state=NORMAL)
	
	for i in range(2):
		dealer_hand.append(global_deck.nextcard())
		player_hand.append(global_deck.nextcard())
	for i in range(2,6):
		dealer_hand_display[i].display('blank')
		player_hand_display[i].display('blank')
	player_hand_display[0].display('front', player_hand[0].ID)
	player_hand_display[1].display('front', player_hand[1].ID)
	dealer_hand_display[0].display('back')
	dealer_hand_display[1].display('front', dealer_hand[1].ID)

	# extra credit, checks for "Blackjack"
	if (check_blackjack(dealer_hand)) or (check_blackjack(player_hand)):
		dealer_hand_display[0].display('front', dealer_hand[0].ID)
		if (check_blackjack(dealer_hand)):
			win_process('dealer')
		elif (check_blackjack(player_hand)):
			win_process('player')

def hit():
	'''
	"hit" player, flipping card and adding it to player_hand.
	Checks to see if player goes over 21.
	'''
	global dealer_hand
	global player_hand
	global global_deck
	global dealerwin_count

	current_bet.config(state=DISABLED)
	current_bet.delete(0,END)

	player_hand.append(global_deck.nextcard())
	player_hand_display[len(player_hand)-1].display('front', player_hand[len(player_hand)-1].ID)
	if total(player_hand) > 21:
		win_process('dealer')
	# extra credit, initiates win sequence if a 5-card win is detected
	if check_5cardwin(player_hand):
		win_process('player')

def pass_end():
	'''
	"passes", meaning that the dealer draws until their hand totals
	17, at which point scores are compared and a winner is announced.
	'''
	global dealer_hand
	global player_hand
	global global_deck
	global dealerwin_count
	global playerwin_count

	current_bet.config(state=DISABLED)

	index = 2
	dealer_hand_display[0].display('front', dealer_hand[0].ID)
	while total(dealer_hand) < 17:
		dealer_hand.append(global_deck.nextcard())
		dealer_hand_display[index].display('front', dealer_hand[index].ID)
		index += 1
	# extra credit, initiates win sequence if a 5-card win is detected
	if check_5cardwin(dealer_hand):
		win_process('dealer')
	else:
		if (total(dealer_hand) > 21) or (total(dealer_hand) < total(player_hand)):
			win_process('player')
		if (total(dealer_hand) <= 21) and (total(dealer_hand) > total(player_hand)):
			win_process('dealer')
		if total(dealer_hand) == total(player_hand):
			showinfo("Game over", "Tie")

def check_blackjack(hand):
	'''
	checks if hand is a blackjack (2 cards in size, score total = 21)

	args:
		hand = list: list of card objects

	returns:
		boolean value: True if hand is blackjack, False if not
	'''
	if (total(hand) == 21) and (len(hand) == 2):
		return True

def check_5cardwin(hand):
	'''checks if hand is 5 cards in length and totals to 21

	args:
		hand = list: list of card objects

	returns:
		boolean value: True if conditions are true, False if not
	'''
	if (total(hand) == 21) and (len(hand) == 5):
		return True

# buttons
deal_button = Button(root, text='Deal', command=deal)
deal_button.grid(row=2, column=0, pady = 10, columnspan=2)

hit_button = Button(root, text='Hit', command=hit)
hit_button.grid(row=2, column=2, pady = 10, columnspan=2)

pass_button = Button(root, text='Pass', command=pass_end)
pass_button.grid(row=2, column=4, pady = 10, columnspan=2)

# extra credit, keeps score of games
# initializes the score boxes
dealer_header = Label(root, text="Dealer Wins:")
dealer_header.grid(row=0, column=7)

player_header = Label(root, text="Player Wins:")
player_header.grid(row=1, column=7)

dealer_wins = Entry()
dealer_wins.grid(row=0, column=8)
dealer_wins.config(state=NORMAL)
dealer_wins.insert(0,str(0))
dealer_wins.config(state=DISABLED)

player_wins = Entry()
player_wins.grid(row=1, column=8)
player_wins.config(state=NORMAL)
player_wins.insert(0,str(0))
player_wins.config(state=DISABLED)

# extra credit, keeps track of bet balance

# initializes the bet balance
bet_header = Label(root, text="Bet Balance:")
bet_header.grid(row=2, column=7)

bet = Entry()
bet.grid(row=2, column=8)

# initializes the current bet box
current_bet_header = Label(root, text="Current Bet:")
current_bet_header.grid(row=3, column=7)

current_bet = Entry()
current_bet.grid(row=3, column=8)

# initializes the two rows of cards
display_row('dealer')
display_row('player')

if __name__ == '__main__':
    root.mainloop()