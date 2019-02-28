from Card import Card 
from GlobalVar import SUITS
from GlobalVar import RANKS

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

	def shuffle(self):
		pass

	def is_empty(self):
		pass

baralho = Deck()
baralho.print_deck()
print(len(baralho.cards))