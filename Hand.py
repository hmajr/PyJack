"""Arquivo classe Hand
"""
from Card import Card
from Deck import Deck
from GlobalVar import VALUES
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
		self.value += VALUES[card.rank]
		if card.rank == "ace":
			self.ace += 1

		self.adjust_for_ace()


	def adjust_for_ace(self):
		"""Ajusta valor do ÁS quando necessário
		"""
		if self.value > 21 and self.ace > 0:
			for num_times in range(0, self.ace):
				self.value -= 10
				self.ace -= 1
				if self.value < 21:
					break


	def print_hand(self, num_cards = None):


		if num_cards == None:
			num_cards = len(self.cards)

		for card_index in range(0, num_cards):
			for line in range(0, len(self.cards[0].graphCard)):
				print(self.cards[card_index].graphCard[line])

	#	# Implementa print de cartas horizontalmente
	#   # ISSUE: Não lida com caso esconder carta dealer,
	# 	# 		 origem problema: linha append, não iterativo
		# print_list = []
		# for card_index in range(0, num_cards):
		# 	for line in range(0, len(self.cards[0].graphCard)):
		# 		print_list.append(self.cards[card_index].graphCard[line] + " " + self.cards[card_index+1].graphCard[line])
		# for line in range(0, len(print_list)):
		# 	print(print_list[line])

	def hand_points(self):
		return self.value

	def delete_hand(self):
		"""Deleta deck atual
		"""
		del(self.cards[:])
