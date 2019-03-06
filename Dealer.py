from Player import Player

class Dealer(Player):
	"""Classe Dealer"""
	def __init__(self):
		super(Dealer, self).__init__()

	def print_hand(self):
		print("\n=== DEALER'S HAND ===\n")
		self.hand.print_hand()

	def print_partial_hand(self):
		print("\n=== DEALER'S HAND ===\n")
		self.hand.print_hand(1)