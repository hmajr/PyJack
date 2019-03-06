"""Arquivo classe Carta
"""
from GlobalVar import SUITS, SUITS_UNICODE, RANKS


class Card():
	"""Classe Carta
	
	Attributes:
	    cardGraph (list): linhas carta gráfica
	    rank (str): valor da carta
	    suit (str): naipe da carta
	"""

	#Methods
	def __init__(self, suit = None, rank = None):
		"""Construtor carta
		
		Args:
		    suit (None, optional): naipe
		    rank (None, optional): valor
		"""
		self.suit = suit
		self.rank = rank
		self.graphCard = self.generate_graph_card()

	def __str__(self):
		"""Exibe valores da carta
		
		Returns:
		    TYPE: Valores da carta formato: "Naipe: {}, Valor: {}
		"""
		return f"Suit: {self.suit}, Rank: {self.rank}"

	def print_card(self):
		"""Imprime carta gráfica
		"""
		for x in self.cardGraph:
			print(x)

	def generate_graph_card(self):
		"""Gera gráfico da carta
		
		Returns:
		    List: lista de linhas de cada carta
		"""
		offset = 3
		offsetRank = 0
		graph = []

		#borda superior
		graph.append(":"+(offset+len(self.rank)*2)*"'"+":")
		# Ranking superior
		graph.append("| "+self.rank+" "+(len(self.rank)-offsetRank)*" "+" |")
		# Espaço em branco
		graph.append("|"+(offset+len(self.rank)*2)*" "+"|")
		# Naipe
		graph.append("| "+(len(self.rank)-offsetRank)*" "+SUITS_UNICODE[self.suit]+(len(self.rank)-offsetRank)*" "+" |")
		# Espaço em branco
		graph.append("|"+(offset+len(self.rank)*2)*" "+"|")
		# Ranking inferior
		graph.append("| "+(len(self.rank)-offsetRank)*" "+" "+self.rank+" |")
		#borda inferior
		graph.append("'"+(offset+len(self.rank)*2)*"-"+"'")

		return graph

if __name__ == '__main__':
	carta = Card("Spades", "five")
	carta.print_card()
