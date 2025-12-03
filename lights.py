import numpy as np
import random
# Environemnt Varibales

ENVIRONMENT = "RURAL"   # "URBAN" or "RURAL"

if ENVIRONMENT == "RURAL":
    LIGHT_ADJACENT = 0.003
    LIGHT_DIEOFF   = 0.002
    LIGHT_RANDOM   = 0.00005

elif ENVIRONMENT == "URBAN":
    LIGHT_ADJACENT = 0.005
    LIGHT_DIEOFF   = 0.002
    LIGHT_RANDOM   = 0.0008

# LIGHT BEHAVIOR
def newLightAdjacent(grid, gridnew, x, y):
    for a in [-1, 0, 1]:
        for b in [-1, 0, 1]:

            if a == 0 and b == 0:
                continue

            nx = x + a
            ny = y + b

            if nx < 0 or nx >= grid.shape[0] or ny < 0 or ny >= grid.shape[1]:
                continue

            if random.random() <= LIGHT_ADJACENT:
                gridnew[nx, ny] = 2


def newLightDies(grid, gridnew, x, y):
    if random.random() <= LIGHT_DIEOFF:
        gridnew[x, y] = 0


def newLightRandom(grid, gridnew, x, y):
    if random.random() <= LIGHT_RANDOM:
        gridnew[x, y] = 2
