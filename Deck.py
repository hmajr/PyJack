from Card import Card 
from GlobalVar import SUITS
from GlobalVar import RANKS

class Deck():
	"""Baralho de cartas"""
	#ATTRIBUTES
	cards = tuple()
	#METHODS
	def __init__(self):
		for suit in SUITS:
			for rank in RANKS:
				self.cards += (rank,suit)

	def RetriveCard():
		pass

	def Shuffle():
		pass

	def IsEmpty():
		pass

baralho = Deck()
print(baralho.cards)