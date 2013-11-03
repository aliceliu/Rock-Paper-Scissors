from random import randint

options = {0 : 'rock', 1 : 'paper', 2 : 'scissors'}
win = 'Congratulations, you won!'
loss = 'Sorry, but you lost this time.'
tie = "It's a tie, play again!"

def play(player_choice, opponent):
    return functions[player_choice](opponent)

########### Game Logic #############

def get_cpu_choice():
    return options[randint(0,2)]

def rock_chosen(opponent):
        if opponent == 'rock':
            return tie
        elif opponent == 'scissors':
            return win
        return loss

    def paper_chosen(opponent):
        if opponent == 'paper':
            return tie
        elif opponent == 'rock':
            return win
        return loss

    def scissors_chosen(opponent):
        if opponent == 'scissors':
            return tie
        elif opponent == 'paper':
            return win
        return loss
        
functions = {'rock': rock_chosen, 
             'paper': paper_chosen, 
             'scissors': scissors_chosen}