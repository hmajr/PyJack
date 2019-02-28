from GlobalVar import SUITS
from GlobalVar import RANKS

class Card():
	#Attributes
	suit = ""
	rank = ""

	#Methods
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return f"Suit: {self.suit}, Rank: {self.rank}"
