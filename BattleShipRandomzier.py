import random
import numpy as np
import math
import matplotlib.pyplot as plt

unusableints = []           #cells where ships can't be placed
def make_ship(size, board):
    attempts = 0
    while True:         #keeps trying new random ships till one fits in the board
        if attempts > 15:
            print("Placing these ships seems impossible on the board, try again or a different set of ship sizes.")
            break
        dimension = random.randint(0, 1) #1 = horizontal, 0 = vertical
        fail = 0        #if a new ship has nowhere to expand fail will be set to true
        while True:         #generates a new ship "seed" which is placable on the board
            x = random.randint(0, 11)     #x coordinate of ship seed
            y = random.randint(0, 11)     #y coordinate of ship seed
            if board[x, y] == 0:
                break

        newcoords = [(x, y)]          #list to store all the ship locations
        for i in range(size-1):
            if dimension:       #horizontal
                xcoords = []
                for coord in newcoords:     #x coordinates of the ships every block
                    xcoords.append(coord[0])
                possiblex = [min(xcoords), max(xcoords)]    #choosing minimum and maximum points to expand upon
                direction = random.randint(0, 1)     #1 = max, 0 = min
                if direction:       #max
                    if board[possiblex[1]+1, y] == 0:           # == 0 checks if the cell is free
                        newcoords.append((possiblex[1]+1, y))
                    elif board[possiblex[0]-1, y] == 0:
                        newcoords.append((possiblex[0]-1, y))
                    else:
                        fail = 1
                else:               #min
                    if board[possiblex[0]-1, y] == 0:
                        newcoords.append((possiblex[0]-1, y))
                    elif board[possiblex[1]+1, y] == 0:
                        newcoords.append((possiblex[1]+1, y))
                    else:
                        fail = 1
            else:           #vertical
                ycoords = []
                for coord in newcoords:
                    ycoords.append(coord[1])
                possibley = [min(ycoords), max(ycoords)]
                direction = random.randint(0, 1)
                if direction:       #max
                    if board[x, possibley[1]+1] == 0:
                        newcoords.append((x, possibley[1]+1))
                    elif board[x, possibley[0]-1] == 0:
                        newcoords.append((x, possibley[0]-1))
                    else:
                        fail = 1
                else:               #min
                    if board[x, possibley[0]-1] == 0:
                        newcoords.append((x, possibley[0]-1))
                    elif board[x, possibley[1]+1] == 0:
                        newcoords.append((x, possibley[1]+1))
                    else:
                        fail = 1
            if fail:
                break
        if fail == 1:           #if ships fails to find enough space the while loop will restart
            attempts += 1
            continue
        elif len(newcoords) == size:
            break

    return newcoords

def board_set_up(shipsizes):
    grid = np.full(144, 0).reshape(12, 12)  #setting up a 10x10 board, the extra cells are for the border

    for i in range(12):             #setting up the border
        grid[i, 0] = 9
        grid[0, i] = 9
        grid[i, 11] = 9
        grid[11, i] = 9


    ships = []
    for size in shipsizes:
        ship = make_ship(size, grid)
        for block in ship:
            ships.append(block)

            #marking the unusable cells
            unusablecells = [(block[0]-1, block[1]), (block[0]+1, block[1]), (block[0], block[1]-1), (block[0], block[1]+1),
            (block[0]-1, block[1]-1), (block[0]-1, block[1]+1), (block[0]+1, block[1]-1), (block[0]+1, block[1]+1)]
            for coord in unusablecells:
                if grid[coord[0], coord[1]] == 0:
                    grid[coord[0], coord[1]] = 1

    #placing the ships
    for coord in ships:
        grid[coord[0], coord[1]] = 5

    return grid

board = board_set_up([5, 5, 4, 4, 3, 3, 2, 2])

fig, ax = plt.subplots()
img = ax.imshow(board)

plt.show()
