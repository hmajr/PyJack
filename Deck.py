from random import shuffle
from Card import Card 
from GlobalVar import SUITS, RANKS

class Deck():
	"""Baralho de cartas"""
	#ATTRIBUTES
	cards = []
	#METHODS
	def __init__(self):
		"""Generate deck of cards"""
		for suit in SUITS:
			for rank in RANKS:
				self.cards.append(Card(suit, rank)) 

	def print_deck(self):
		for num in range(0, len(self.cards)):
			print( self.cards[num] )

	def retrieve_card(self):
		pass

	def shuffle_deck(self):
		shuffle(self.cards)
		self.cards.reverse()
		shuffle(self.cards)

	def is_empty(self):
		pass


baralho = Deck()
baralho.print_deck()
print(len(baralho.cards))
print("\n\n")
print("Shuffle deck!")
baralho.shuffle_deck()
baralho.print_deck()