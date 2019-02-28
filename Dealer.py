from Player import Player

class Dealer(Player):
	"""Classe Dealer"""
	def __init__(self):
		super(Dealer, self).__init__(name = "Dealer", chips = 0)

	def CheckHandPoints(self):
		if self.HandPoints() < 17:
			pass
			#draw new card
		else:
			pass
			#stop
