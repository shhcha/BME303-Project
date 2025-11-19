import numpy as np
import random

from fontTools.varLib.avar.plan import sanitizeSlant


# function for growth of light sources
# Every graph, there is a _% (high) chance for the adjacent box will get another light.
def newLightAdjacent(grid,rows,cols):
    for i in range(rows):
        for j in range(cols):
            if grid[i,j] == 2: #uhhh we coded light as 2 so whoops
                # what can be affected:
                # [i-1,j+1] <- top right
                # [i-1,j] <- right
                # [i-1, j-1] <- bottom right
                # [i,j+1] <- top middle
                # [i,j-1] <- bottom middle
                # [i+1,j+1] <- top left
                # [i+1,j] <- left
                # [i+1, j-1] <- bottom left
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if x == 0 and y == 0:
                            continue # or pass?
                        else:
                            # here was the og generation: MyGrid = c_Grid(numpy.random.choice([0,1, 2],(30,30),p=[0.95, 0.025, 0.025])
                            # i dont know how to finish this
                            #this is my guess on how to do it
                            r = random.randint(1,10)
                            if r <=6: #filler chance is 60%
                                grid[i + x, j + y] = 2
                            else:
                                continue
                            continue
# Every graph, there is a _% (low) chance that the light will go away.
def newlightDies(grid,x,y):
    # certain percentage that it'll turn black
    r = random.randint(1,10)
    if r <= 3: #just making the chance it'll turn black 30% as a filler
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