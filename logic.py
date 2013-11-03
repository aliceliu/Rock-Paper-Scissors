from random import randint

options = {2 : 'rock', 3 : 'paper', 4 : 'scissors'}
win = 1
loss = 0
tie = 'tie'

def game(player_choice):

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
        
    functions = {'rock':rock_chosen, 'paper':paper_chosen,
     'scissors':scissors_chosen}
    cpu_choice = options[randint(2,4)]
    return functions[player_choice](cpu_choice)
