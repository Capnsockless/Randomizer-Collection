import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def random_neighbor(x, y):
    possiblecells = [(x, y), (x-1, y), (x+1, y), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y+1), (x-1, y-1), (x-1, y+1)]
    for coord in possiblecells:
        if grid[coord[0], coord[1]] == 1:       #if a cell is already a border cell it will be removed
            possiblecells.remove(coord)         #from the possible cells
    output = random.choice(possiblecells)       #taking a random cell out of the possibles
    return output[0], output[1]


def update(frameNum, img, grid, N):

    newgrid = grid.copy()
    for i in range(N):
        for j in range(N):

            if grid[i, j] == 4:
                death = random.randint(0, 1)
                if death:           #50% for the pixel to die
                    newgrid[i, j] = 0
                x, y = random_neighbor(i, j)    #random direction to spread in
                newgrid[x, y] = 4
            elif grid[i, j] == 5:
                death = random.randint(0, 1)
                if death:
                    newgrid[i, j] = 0
                if newgrid[i, j] == 4 and grid[i, j] != 4:      #if both colors are trying to claim the same pixel
                    victor = random.randint(0, 1)               #it will be settled with a 50/50 chance
                    if victor:
                        x, y = random_neighbor(i, j)
                        newgrid[x, y] = 5
                else:
                    x, y = random_neighbor(i, j)
                    newgrid[x, y] = 5


    img.set_data(newgrid)
    grid[:] = newgrid[:]
    return img

grid = np.full(6724, 0).reshape(82, 82) #80x80 board, the extra 2 is for the border

for i in range(82):         #setting up borders on the edges
    grid[i, 0] = 1
    grid[0, i] = 1
    grid[i, 81] = 1
    grid[81, i] = 1


grid[20, 60] = 4        #setting the starting pixels
grid[60, 20] = 5


fig, ax = plt.subplots()        # set up animation
img = ax.imshow(grid)
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, 81), frames = 10, interval=50, save_count=50)


plt.show()
