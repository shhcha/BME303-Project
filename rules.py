import numpy as np
import moth
import math


def moth_death(grid, x, y ):
    lightDist = moth.findClosestEntity(grid,x,y, entityToFind ='L')
    if math.sqrt((lightDist[0])**2 + lightDist[1]**2) >= 2:
        return 0
    else:
        math.sqrt((lightDist[0]) ** 2 + lightDist[1] ** 2) < 2
        return 1

def moth_birth(grid, x, y):
    mothDist = moth.findClosestEntity(grid, x, y, entityToFind = 'M')
    if math.sqrt((mothDist[0])**2 + mothDist[1]**2) >=2:
        # find a nearby 0 and replace it to be a 1 somehow
        pass
    if math.sqrt((mothDist[0])**2 + mothDist[1]**2) <2:
        return 2



def lights():
    pass



def dimming():
    pass
def mothMove():
    pass

def update(): #a function that checks what square it is, and calls the other functions accordingly
    pass