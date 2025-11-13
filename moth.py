import numpy

#Returns tuple(x,y) delta to the nearest light 
def findClosestLight(grid:numpy.ndarray, mothX:int, mothY:int):
    shape = grid.shape
    for i in range(-shape[0],shape[0]):
        if (mothX+i >= shape[0]) or (mothX+i < 0):
            continue

        for j in range(-shape[1],shape[1]):
            if (mothY+j >= shape[1]) or (mothY+j < 0):
                continue

            if (grid[mothX+i][mothY+j] == 1):
                return (i,j)
                
def nextMove(grid:numpy.ndarray, mothX:int, mothY:int):
    deltaX, deltaY = 0,0

    return (deltaX, deltaY)