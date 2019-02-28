from GlobalVar import SUITS
from GlobalVar import RANKS

class Card():
	#Attributes
	suit = ""
	rank = ""

	#Methods
	def __init__(self):
		pass

	def __init__(self, suit = None, rank = None):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return f"Suit: {self.suit}, Rank: {self.rank}"

	def print_card():
		pass