from Player import Player

class Dealer(Player):
	"""Classe Dealer"""
	def __init__(self):
		super(Dealer, self).__init__()

	def CheckHandPoints(self):
		if self.HandPoints() < 17:
			pass
			#draw new card
		else:
			pass
			#stop
	def print_partial_hand():
		self.hand.print_hand(1)