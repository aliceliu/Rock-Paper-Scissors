from random import randint

cpu_options = {0 : 'rock', 1 : 'paper', 2 : 'scissors'}
win = 'Congratulations, you won!'
loss = 'Sorry, but you lost this time.'
tie = "It's a tie, play again!"

results = {('rock', 'rock'): tie,
           ('rock', 'scissors'): win,
           ('rock', 'paper'): loss,
           ('scissors', 'scissors'): tie,
           ('scissors', 'paper'): win,
           ('scissors', 'rock'): loss,
           ('paper', 'paper'): tie,
           ('paper', 'rock'): win,
           ('paper', 'scissors'): loss
                    }

def get_random_choice():
    return cpu_options[randint(0,2)]

def play(player_choice, opponent):
    return results[(player_choice, opponent)]




