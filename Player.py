class Player():
	"""Classe do jogador"""
	#ATTRIBUTES
	name = ""
	chips = 0
	hand = []


	#METHODS
	def __init__(self, name, chips = 1000):
		self.name = name

	def take_one_card(self):
		pass

	def make_bid(self):
		pass

	def hand_points(self):
		pass