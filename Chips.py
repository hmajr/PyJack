"""Summary
"""
from GlobalVar import DEFAULT_CHIPS

class Chips():
	"""Classe de fichas
	
	Attributes:
	    bet (int): quantidade de aposta da rodada atual
	    total (TYPE): total de fichas
	"""
	def __init__(self, chips):
		"""Inicializa classe com valores padrões
		"""
		self.total = chips
		self.bet = 0

	def win_bet(self):
		"""Soma fichas ganhas ao total
		"""
		self.total += self.bet
		
	def lose_bet(self):
		"""Subtrai fichas do total atual
		"""
		self.total -= self.bet