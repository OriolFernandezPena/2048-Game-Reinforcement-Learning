import numpy as np

def LeftMove(game):
    # First we colapse to the left side but we don't sum yet
    game_t1 = []
    for row in game:
        new_row = []
        for el in row:
            if el != 0:
                new_row.append(el)
        while len(new_row) < 4:
            new_row.append(0)
        game_t1.append(new_row)
    # We operate:
    for row in game_t1:
        if row[1] == 0:
            continue
        else:
            if row[1] == row[0]:
                row[0] += row[1]
                row[1:3] = row[2:4]
                row[3] = 0
            if row[2] == row[1]:
                row[1] += row[2]
                row[2] = row[3]
                row[3] = 0
            if row[3] == row[2]:
                row[2] += row[3]
                row[3] = 0
        
    return np.array(game_t1)

def RightMove(game):
    game_left = LeftMove(np.array([row[::-1] for row in game]))
    return np.array([row[::-1] for row in game_left])

def DownMove(game):
    return RightMove(game.T).T

def UpMove(game):
    return LeftMove(game.T).T

def HorCollapsable(game):
    for row in game:
        if (row[0] == row[1])|(row[1] == row[2])|(row[2] == row[3]):
            return True
    return False

def VerCollapsable(game):
    return HorCollapsable(game.T)
    
def isCollapsable(game):
    return (VerCollapsable(game))|(HorCollapsable(game))
    
