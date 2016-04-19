import random


def shuffled_deck():
	basic_deck = range(2, 15) * 4
	random.shuffle(basic_deck)
	return basic_deck
deck = shuffled_deck()

player_name = raw_input("What is your name, player 1?")
player_name2=raw_input("Whats your name, player 2?")

play_name_score = 0
play_name_score2 = 0

def player_turn(player_name):
	card= deck.pop()
	print player_name,'drew card', card
	return str(card)
player_turn(player_name)
player_turn(player_name2)

while deck:
	if player_turn(player_name) > player_turn(player_name2):
		player_name_score = player_name_score = 1
	elif player_turn(player_name2)> player_turn(player_name):
		player_name_score2 = play_name_score2


	#This code needs more cards to be drawn and then added to see who wins in results
