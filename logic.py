from random import choice

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

def randomchoice():
    return choice(['rock','paper','scissors'])

def play(player_choice, opponent):
    return results[(player_choice, opponent)]




