"""Arquivo classe Hand
"""
from Card import Card
from Deck import Deck

class Hand():
	"""Representa a mão do jogador
	
	Attributes:
	    ace (int): flag para controle do valor do ÁS
	    cards (list): cartas da mão de jogo
	    value (int): pontuação da mão atual
	"""
	def __init__(self):
		"""Inicializa mão com valores padrões
		"""
		self.cards = []
		self.value = 0
		self.ace = 0

	def add_card(self, card):
		"""Adciona uma carta a mão atual
		
		Args:
		    deck (Card Class): carta a adcionar
		"""
		self.cards.append(card)

	def adjust_for_ace(self):
		"""Ajusta valor do ÁS quando necessário
		"""
		pass