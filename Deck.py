"""Arquivo classe Deck
"""
import random 
from Card import Card
from GlobalVar import SUITS, RANKS


class Deck():
	"""Baralho de cartas
	
	Attributes:
	    cards (list): lista de cartas do baralho
	"""
	#ATTRIBUTES
	cards = []

	#METHODS
	def __init__(self):
		"""Gera deck de cartas
		"""
		if not(self.is_empty()):
			self.delete_deck()

		for suit in SUITS:
				for rank in RANKS:
					self.cards.append(Card(suit, rank))

	def shuffle_deck(self):
		"""Embaralha cartas do baralho
		"""
		random.shuffle(self.cards)
		self.cards.reverse()
		random.shuffle(self.cards)
	
	def deal(self):
		"""Retira carta do baralho
		Returns:
		    Card: carta do baralho
		"""
		return self.cards.pop()


#MY FUNCTIONS 
	def print_deck(self):
		"""Summary
		"""
		for num in range(0, len(self.cards)):
			print( self.cards[num] )

	def is_empty(self):
		"""Verifica se deck está vazio
		
		Returns:
		    bool: verdadeiro se deck vazio
		"""
		return len(self.cards) == 0

	def delete_deck(self):
		"""Deleta deck atual
		"""
		del(self.cards[:])

if __name__ == '__main__':
	
	baralho = Deck()

	#Teste print cartas ordenadas baralho
	baralho.print_deck()
	print(len(baralho.cards))
	print("\n\n")

	print("Shuffle deck!")
	baralho.shuffle_deck()
	baralho.print_deck()

	baralho = Deck()