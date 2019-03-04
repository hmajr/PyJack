from GameEngine import *
from GameScreen import *
from Deck import Deck
from Player import Player
from Dealer import Dealer

"""Loop principal do jogo
"""
# while True:
if True:
	# Print an opening statement
	title_screen()
  	# Create & shuffle the deck, deal two cards to each player
	gameDeck = Deck()
	gameDeck.shuffle_deck()
  	# Set up the Player's chips
	player = Player()
	dealer = Dealer()

  	# Prompt the Player for their bet
	player.make_bid()
 #    print()
  	# Show cards (but keep one dealer card hidden)
	# Dealer.print_partial_hand()
	# Player.print_hand()
    	
  	# while playing:  # recall this variable from our hit_or_stand function
  	# while playing:   
  	    # Prompt for Player to Hit or Stand
#   	    hit_or_stand()
	    
  	    # Show cards (but keep one dealer card hidden)
			
	   	    
	   	    # If player's hand exceeds 21, run player_busts() and break out of loop
	   	    

  	        # break

  	# If Player hasn't busted, play Dealer's hand until Dealer reaches 17
	
	
  	    # Show all cards
	
  	    # Run different winning scenarios
	    
	
  	# Inform Player of their chips total 
	
  	# Ask to play again

  	    # break