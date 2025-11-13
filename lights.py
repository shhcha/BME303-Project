import numpy as np

# function for growth of light sources
# Every graph, there is a _% (high) chance for the adjacent box will get another light.
def newLightAdjacent():
    for i in range(rows):
        for j in range(cols):
            if grid[i,j] == 1:
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
                            # here was the og generation: MyGrid = c_Grid(numpy.random.choice([0,1, 2],(30,30),p=[0.95, 0.025, 0.025]))
                            # i dont know how to finish this
                            continue
# Every graph, there is a _% (low) chance that the light will go away.
def newlightDies:
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 1:
                # certain percentage that itll turn black
# Every graph, there is a _% (unsure) chance that another light will appear randomly.
def newLightRandom:
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 1:
                # percentage that a new might appear