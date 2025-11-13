import numpy

#Returns tuple(x,y) delta to the nearest light 
def findClosestEntity(grid:numpy.ndarray, mothX:int, mothY:int, entityToFind:str='L'):
    shape = grid.shape
    if entityToFind == 'L':
        entityToFind = 2
    elif entityToFind == 'M':
        entityToFind = 1
    else:
        raise TypeError(f"EntityType {entityToFind} is not valid")

    for i in range(-shape[0],shape[0]): 
        if (mothX+i >= shape[0]) or (mothX+i < 0):
            continue

        for j in range(-shape[1],shape[1]):
            if (mothY+j >= shape[1]) or (mothY+j < 0):
                continue

            if (grid[mothX+i][mothY+j] == entityToFind):
                return (i,j)

def nextMove(grid:numpy.ndarray, mothX:int, mothY:int):
    deltaX, deltaY = 0,0
    lightRelPos = findClosestEntity(grid,mothX,mothY,'L')
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

    deltaX += numpy.random.choice((-1,0,1))
    deltaY += numpy.random.choice((-1,0,1))
    
    return (deltaX, deltaY)