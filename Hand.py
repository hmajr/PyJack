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

	def print_hand(num_cards = None):
		if num_cards == None:
			num_cards = len(self.card)

		for num_line in range(0,len(self.card.graphCard)):
			for num_cards in range(0,num_cards):
				print(self.card[num_card].graphCard[num_line])

	def hand_points(self):
		return self.value
