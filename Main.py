from GameScreen import *
from Deck import Deck
from Player import Player
from Dealer import Dealer
from GlobalVar import playing, DEFAULT_CHIPS
from os import system

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
	hand.add_card(deck.deal())

def hit_or_stand(deck, hand):
	global playing

	try:
		status = input("'hit' ou  'stand'? ")

		if status != "hit"  and status != "stand":
			raise InvalidActionError
	except InvalidActionError:
		print("Comando digitado: " + status)
		print("Comando invalido! Escolha 'hit' ou 'stand'.\n")
	else:
		if status == "hit":
			hit(deck, hand)
		if status == "stand":
			playing = False

#END GAME SCENARIOS
def player_wins():

    player_win_screen()

def player_busts():
    player_busted_screen()
    
def dealer_busts():
    dealer_busted_screen()
    
def dealer_wins():
    player_lose_screen()
    
def push():
    draw_game()

def new_game():
	"""Pergunta se deseja jogar novamente
	"""
	pass
	#pergunta P1 jogar novamente
		#N : PLAYING = FALSE


#GameEngine EXCEPTIONS
class InvalidActionError(Exception):
	"""docstring for InvalidActionError"""
	def __init__(self):
		pass


"""GAME LOOP

Main game loop
"""
if __name__ == '__main__':
	"""Loop principal do jogo
	"""
	title_screen()

  	# Set up the Player's chips
	player = Player(DEFAULT_CHIPS)
	dealer = Dealer()

	while True:
		# Print an opening statement
	  	
	  	# Create & shuffle the deck, deal two cards to each player
		gameDeck = Deck()
		gameDeck.shuffle_deck()


	  	# Prompt the Player for their bet
		player.make_bid()

		#Distribute playing cards
		player.take_card(gameDeck, 2)
		dealer.take_card(gameDeck, 2)

	  	# Show cards (but keep one dealer card hidden)
		dealer.print_partial_hand()
		player.print_hand()


	  	# recall this variable from our hit_or_stand function
		while playing:   
	  	    # Prompt for Player to Hit or Stand
			hit_or_stand(gameDeck, player.hand)
		    
	  	    # Show cards (but keep one dealer card hidden)
			dealer.print_partial_hand()
			player.print_hand()

	   	   	# If player's hand exceeds 21, run player_busts() and break out of loop
			if player.hand.hand_points() > 21:
				break

		if player.hand.hand_points() < 21:
			while dealer.hand.hand_points() < 17:		
				dealer.take_card(gameDeck)
  			    
  			    # Show all cards
				dealer.print_hand()
				player.print_hand()
					
	    # Run different winning scenarios
		# system("cls")
		dealer.print_hand()
		print(str(dealer.hand.hand_points()))

		player.print_hand()
		print(str(player.hand.hand_points()))
		TRASH = input()

		if player.hand.hand_points() > 21:
			player.chips.lose_bet()
			player_busts()
		elif dealer.hand.hand_points() > 21:
			player.chips.win_bet()
			dealer_busts()
		elif player.hand.hand_points() > dealer.hand.hand_points():
			player.chips.win_bet()
			player_wins()
		elif player.hand.hand_points() < dealer.hand.hand_points():
			player.chips.lose_bet()
			dealer_wins()
		elif player.hand.hand_points() == dealer.hand.hand_points():
			push()

		
	  	# Inform Player of their chips total 
		print("TOTAL CHIPS: " + str(player.chips.total))

	  	# Ask to play again
		try:
			print("Play again (sim/nao)? ")
			replay = input()
			
			if replay != "sim" and replay != "nao":
				raise Exception
		except Exception as e:
			print(replay)
			print("Digite 'sim' para SIM, ou 'nao' para NÃO")
			break
		else:
			if replay == "sim":
				system("cls")
				player.hand.delete_hand()
				dealer.hand.delete_hand()

				#RESET CONDITIONALS STATES
				playing = True
				player = Player(player.chips.total)
				dealer = Dealer()
			elif replay == "nao":
				thanks_playing_screen()
				break
	#fim TRUE game loop