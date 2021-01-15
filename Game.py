# import random
import numpy as numpy
from GameSource.Moves import *
from GameSource.Initializer import new_game, new_number

if __name__ == '__main__':
    funciones = {'u' : UpMove, 'd' : DownMove, 'r' : RightMove, 'l' : LeftMove}
    game = new_game()
    # game = np.array([[0,4,16,64], [2,8,128,2], [4,32,64,512],[8,16,32,1024]])
    print(game)
    while True:
        print('Play:')
        move = input()
        if move == 'End':
            break
        while move not in ['u', 'd', 'r', 'l']:
            print('Type u, d, r or l.')
            move = input()
        game_1 = funciones[move](game)
        if (game_1 == game).all():
            print('That move is not possible.')
            continue
        game = new_number(game_1, False)
        print(game)
        if isCollapsable(game) == False:
            print('Game over!')
            break
