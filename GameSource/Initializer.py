import numpy as np

def new_game():
    # Generating position of the first two numbers
    pos1, pos2 = np.random.randint(0,16), np.random.randint(0,16)
    i1, i2 = int(pos1 / 4), int(pos2 / 4)
    j1, j2 = pos1 % 4, pos2 % 4
    # Generating the numbers for each position
    n1, n2 = 2*np.random.binomial(1, 0.13) + 2, 2*np.random.binomial(1, 0.13) + 2
    game = np.zeros((4,4))
    game[i1,j1],game[i2,j2] = n1, n2
    return game
    
def new_number(game, blocked_move):
    if blocked_move:
        # When the last move wasn't possible no new number is generated
        return game
    blank_spaces = [[i, j] for i in range(4) for j in range(4) if game[i, j] == 0]
    # print(blank_spaces)
    v = np.random.randint(len(blank_spaces))
    i, j = blank_spaces[v]
    game_1 = game
    game_1[i, j] = 2*(np.random.binomial(1, 0.13) + 1)
    return game_1
    
def blank_spaces(matrix):
    return len([el for row in matrix for el in row if el == 0])
            
            
if __name__ == '__main__':
    game = new_game()
    print(game)
    while True:
        game = new_number(game, False)
        print(game)
        if len([el for row in game for el in row if el == 0]) == 0:
            break

