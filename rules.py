import numpy as np
import moth
import math
class rules:
    def __init__(self, grid):
        grid = self.grid

    def moth_death(self, grid, x, y, ):
        lightDist = moth.findClosestLight(grid,x,y)
        if math.sqrt((lightDist[0])**2 + lightDist[1]**2) >= 2:
            return 0
        elif:
            math.sqrt((lightDist[0]) ** 2 + lightDist[1] ** 2) < 2
            return 1

    def moth_birth(self):



    def lights(self):





    def dimming(self):


    def leUpdate(self): #a function that checks what square it is, and calls the other functions accordingly