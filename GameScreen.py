from os import system
def print_table(player, dealer):
	dealer.print_partial_hand()
	player.print_hand()

def title_screen():
	# Clean screen
	system("cls")
	print("======================================")
	print("  _____            _            _     ")
	print(" |  __ \          | |          | |    ")
	print(" | |__) |   _     | | __ _  ___| | __ ")
	print(" |  ___/ | | |_   | |/ _` |/ __| |/ / ")
	print(" | |   | |_| | |__| | (_| | (__|   <  ")
	print(" |_|    \__, |\____/ \__,_|\___|_|\_\ ")
	print("         __/ |                        ")
	print("        |___/                         ")
	print("======================================")
	print("\n")
	print("\n")

def player_win_screen():
	# Clean screen
	system("cls")
	print("__   __            _    _ _       ")
	print("\ \ / /           | |  | (_)      ")
	print(" \ V /___  _   _  | |  | |_ _ __  ")
	print("  \ // _ \| | | | | |/\| | | '_ \ ")
	print("  | | (_) | |_| | \  /\  / | | | |")
	print("  \_/\___/ \__,_|  \/  \/|_|_| |_|")
                              
def player_lose_screen():
	# Clean screen
	system("cls")
	print("__   __            _                     ")
	print("\ \ / /           | |                    ")
	print(" \ V /___  _   _  | |     ___  ___  ___  ")
	print("  \ // _ \| | | | | |    / _ \/ __|/ _ \ ")
	print("  | | (_) | |_| | | |___| (_) \__ \  __/ ")
	print("  \_/\___/ \__,_| \_____/\___/|___/\___| ")

def player_busted():
	# Clean screen
	system("cls")
	print("__   __           ______           _           _ ")
	print("\ \ / /           | ___ \         | |         | |")
	print(" \ V /___  _   _  | |_/ /_   _ ___| |_ ___  __| |")
	print("  \ // _ \| | | | | ___ \ | | / __| __/ _ \/ _` |")
	print("  | | (_) | |_| | | |_/ / |_| \__ \ ||  __/ (_| |")
	print("  \_/\___/ \__,_| \____/ \__,_|___/\__\___|\__,_|")

if __name__ == '__main__':
	# title_screen()
	# player_busted()
	print(u"\u2660")