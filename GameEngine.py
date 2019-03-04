
#MAIN GAME FUNCTIONS

	  
#SHOW CARDS
def show_some(player,dealer):
    
    pass
    
def show_all(player,dealer):
    
    pass

#ACTIONS
def take_bet():
	"""Recebe as apostas
	"""
	pass

def hit(deck, hand):
	"""
	Retira carta do deck
	Adciona a mão do jogador atual.
	Verifica mão < 21
	
	Args:
	    deck (Deck Class): recebe baralho de cartas do jogo atual
	    hand (Hand Class): recebe mão do jogador
	"""

def hit_or_stand():
	global playing

	while playing:
		status = input("'hit' ou  'stand'? ")

		if status == "hit":
			hit(baralho, player.hand)
		elif status == "stand":
			break
		else:
			print("Status errado. Digite sem as aspas")
	pass

#END GAME SCENARIOS
def player_busts():
    pass

def player_wins():
    pass

def dealer_busts():
    pass
    
def dealer_wins():
    pass
    
def push():
    pass

def new_game():
	"""Pergunta se deseja jogar novamente
	"""
	pass
	#pergunta P1 jogar novamente
		#N : PLAYING = FALSE

if __name__ == '__main__':
	game_loop()