from Card import Card
from Deck import Deck

class Hand():
	"""Representa a mão do jogador"""
	def __init__(self):
		self.cards = []
		self.value = 0
		self.ace = 0

	def add_card(self, deck):
		self.cards.append(deck.retrive_card())

	def adjust_for_ace(self):
		pass