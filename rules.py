import numpy as np
import moth
import math

class rules:
    def __init__(self, grid):
        grid = self.grid

    def moth_death(self, grid, x, y, ):
        lightDist = moth.findClosestEntity(grid,x,y, entityToFind ='L')
        if math.sqrt((lightDist[0])**2 + lightDist[1]**2) >= 2:
            return 0
        elif:
            math.sqrt((lightDist[0]) ** 2 + lightDist[1] ** 2) < 2
            return 1

    def moth_birth(self):
        mothDist = moth.findClosestEntity(grid, x, y, entityToFind = 'M')
        if math.sqrt((mothDist[0])**2 + mothDist[1]**2) >=2:
            # find a nearby 0 and replace it to be a 1 somehow

        if math.sqrt((mothDist[0])**2 + mothDist[1]**2) <2:
            return 2



    def lights(self):



    def dimming(self):

    def mothMove(self):


    def leUpdate(self): #a function that checks what square it is, and calls the other functions accordingly