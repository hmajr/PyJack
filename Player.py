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
	def take_one_card(self):
		pass

	def make_bid(self):
		while True:
			try:
				print(f"Total de fichas: {self.chips.total}")
				bid = int(input("Qual a sua aposta? "))
				if bid > self.chips.total:
					print("")
					raise OverQuantityError()
				elif bid == 0:
					raise ZeroBidError()
				else: 
					self.chips.bet = bid
			except ValueError:
				print("Insira um número inteiro")
				continue
			except OverQuantityError:
				print("Quantidade de fichas indisponível")
				continue
			except ZeroBidError:
				print("Aposta deve ser maior que 0")
				continue
			except :
				print("Tente novamente!!!")
			else:
				break

	def print_hand():
		self.hand.print_hand()

#Player Exceptions
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

