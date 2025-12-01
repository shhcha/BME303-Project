import numpy as np
import random

from fontTools.varLib.avar.plan import sanitizeSlant


# function for growth of light sources
# Every graph, there is a _% (high) chance for the adjacent box will get another light.
def newLightAdjacent(grid,x,y):
    for a in [-1, 0, 1]:
        for b in [-1, 0, 1]:
            if a == 0 and b == 0: #original point
                continue
            if x+a >= grid.shape[0] or y+b >= grid.shape[1]:
                continue
            if x+a < 0 or y+b < 0:
                continue
            else:
                # here was the og generation: MyGrid = c_Grid(numpy.random.choice([0,1, 2],(30,30),p=[0.95, 0.025, 0.025])
                r = random.random()
                if r <= 0.0095: #filler chance is 5%
                    grid[x + a, y + b] = 2
                else:
                    continue
                continue
# Every graph, there is a _% (low) chance that the light will go away.
def newLightDies(grid,x,y):
    # certain percentage that it'll turn black
    r = random.random()
    if r <= 0.005: #just making the chance it'll turn black 10% as a filler
        grid[x,y] = 0
    else:
        pass #we don't need to check the rows and columns since the update function will do that anyways

# Every graph, there is a _% (unsure) chance that another light will appear randomly.
def newLightRandom(grid,x,y):
    # percentage that a new might appear
    # For now a filler % is 50
    r = random.randint(1,10)
    if r <=5:
        grid[x, y] = 2
    else:
        pass



# yay