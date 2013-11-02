from random import randint

options = {'rock' : 0, 'paper': 1, 'scissors' : 2}
win = 1
loss = 0
tie = 'tie'

def game(selection):
		def rocks(opponent):
			if opponent == 0:
				return tie

		player_choice = options[selection]
		cpu_choice = randint(range(3))
		if player == 0
