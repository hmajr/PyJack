from GlobalVar import SUITS, SUITS_UNICODE, RANKS

class Card():
	#Attributes
	suit = ""
	rank = ""
	cardGraph = []

	#Methods
	def __init__(self, suit = None, rank = None):
		self.suit = suit
		self.rank = rank
		self.cardGraph = self.generate_graph_card()

	def __str__(self):
		return f"Suit: {self.suit}, Rank: {self.rank}"

	def print_card(self):
		for x in self.cardGraph:
			print(x)

	def generate_graph_card(self):
		offset = 3
		offsetRank = 0
		graph = []

		graph.append(":"+(offset+len(self.rank)*2)*"'"+":")
		graph.append("| "+self.rank+" "+(len(self.rank)-offsetRank)*" "+" |")
		graph.append("|"+(offset+len(self.rank)*2)*" "+"|")
		graph.append("| "+(len(self.rank)-offsetRank)*" "+SUITS_UNICODE[self.suit]+(len(self.rank)-offsetRank)*" "+" |")
		graph.append("|"+(offset+len(self.rank)*2)*" "+"|")
		graph.append("| "+(len(self.rank)-offsetRank)*" "+" "+self.rank+" |")
		graph.append("'"+(offset+len(self.rank)*2)*"-"+"'")

		return graph

if __name__ == '__main__':
	carta = Card("Spades", "five")
	carta.print_card()
