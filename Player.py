from Chips import Chips
from Hand import Hand

# from Exception import Exception

class Player():
	"""Classe do jogador"""
	#ATTRIBUTES
	def __init__(self):
		self.chips = Chips()
		self.hand = Hand()

	#METHODS
	def take_card(self, deck, num_cards = 1):
		for num in range(0,num_cards):
			self.hand.add_card(deck.deal())

	def make_bid(self):
		while True:
			try:
				print(f"Total de fichas: {self.chips.total}")
				bid = int(input("Qual a sua aposta? "))
				if bid > self.chips.total:
					raise OverQuantityError()
				elif bid == 0:
					raise ZeroBidError()
				else: 
					self.chips.bet = bid
			except ValueError:
				print("\nInsira um número inteiro")
				continue
			except OverQuantityError:
				print("\nQuantidade de fichas indisponível")
				continue
			except ZeroBidError:
				print("\nAposta deve ser maior que 0")
				continue
			else:
				self.chips.bet = bid
				break

	def print_hand(self):
		print("\n=== PLAYER'S HAND ===\n")
		self.hand.print_hand()

#PLAYER EXCEPTIONS
class OverQuantityError(Exception):
	"""docstring for QuantityError"""
	def __init__(self):
		pass

class ZeroBidError(Exception):
	"""docstring for ZeroBidError"""
	def __init__(self):
		pass
		

if __name__ == '__main__':
	player = Player()

	player.make_bid()

	player.print_hand()

