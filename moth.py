import numpy

#Returns tuple(x,y) delta to the nearest light 
def findClosestLight(grid:numpy.ndarray, mothX:int, mothY:int):
    shape = grid.shape      
    for i in range(-shape[0],shape[0]): #So we check all 
        if (mothX+i >= shape[0]) or (mothX+i < 0):
            continue

        for j in range(-shape[1],shape[1]):
            if (mothY+j >= shape[1]) or (mothY+j < 0):
                continue

            if (grid[mothX+i][mothY+j] == 1):
                return (i,j)

def findClosestMoth(grid:numpy.ndarray, mothX:int, mothY:int):
    shape = grid.shape      
    for i in range(-shape[0],shape[0]): #So we check all 
        if (mothX+i >= shape[0]) or (mothX+i < 0):
            continue

        for j in range(-shape[1],shape[1]):
            if (mothY+j >= shape[1]) or (mothY+j < 0):
                continue

            if (grid[mothX+i][mothY+j] == 0):
                return (i,j)

def nextMove(grid:numpy.ndarray, mothX:int, mothY:int):
    deltaX, deltaY = 0,0
    lightRelPos = findClosestLight(grid,mothX,mothY)
    print(lightRelPos)
    max_movement = 5
    
    factorX = -1 if lightRelPos[0] < 0 else 1
    factorY = -1 if lightRelPos[1] < 0 else 1
    
    deltaX = abs(lightRelPos[0])
    deltaY = abs(lightRelPos[1])

    if (abs(deltaX) >= max_movement):
        deltaX = round(max_movement * factorX)
    else:
        deltaX = round(deltaX*factorX)

    if (abs(deltaY) >= max_movement):
        deltaY = round(max_movement * factorY)
    else:
        deltaY = round(deltaY*factorY)
    return (deltaX, deltaY)