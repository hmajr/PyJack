import GameScreen
from Deck import Deck

#MAIN GAME FUNCTIONS
def init_game():
	"""Iniciliza jogo, montando deck e embaralhando cartas
	"""

	gameDeck = Deck()
	gameDeck.shuffle_deck()
	
	return gameDeck

def game_loop():
	"""Loop principal do jogo
	"""
	# while True:
    # Print an opening statement

    
    # Create & shuffle the deck, deal two cards to each player

    
        
    # Set up the Player's chips
    
    
    # Prompt the Player for their bet

    
    # Show cards (but keep one dealer card hidden)

    
    # while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        
        
        # Show cards (but keep one dealer card hidden)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        

            # break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    
    
        # Show all cards
    
        # Run different winning scenarios
        
    
    # Inform Player of their chips total 
    
    # Ask to play again

        # break

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

