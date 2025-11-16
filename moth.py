import numpy

### Rules
def tryDeath(grid:numpy.ndarray, mothPos:numpy.ndarray ):
    lightDist = findClosestEntity(grid, mothPos, entityToFind ='L')
    if math.sqrt((lightDist[0])**2 + lightDist[1]**2) >= 2:
        return 0
    else:
        math.sqrt((lightDist[0]) ** 2 + lightDist[1] ** 2) < 2
        return 1

def tryBirth(grid:numpy.ndarray, mothPos:numpy.ndarray):
    mothDist = moth.findClosestEntity(grid, mothPos, entityToFind = 'M')
    if math.sqrt((mothDist[0])**2 + mothDist[1]**2) >=2:
        # find a nearby 0 and replace it to be a 1 somehow
        pass
    if math.sqrt((mothDist[0])**2 + mothDist[1]**2) <2:
        return 2

### Movement
def _Move(grid:numpy.ndarray, mothPos:numpy.ndarray, mothDeltaPos:numpy.ndarray):
    try:
        grid[tuple(mothPos+mothDeltaPos)] = 1
        grid[tuple(mothPos)] = 0
    except IndexError:
        print(f"Cannot move moth ")

def tryMovement(grid:numpy.ndarray, mothPos:numpy.ndarray):
    _Move(grid, mothPos, findNextMove(grid, mothPos))

#Returns ndarray(x,y) delta to the nearest light 
def findClosestEntity(grid:numpy.ndarray, mothPos:numpy.ndarray, entityToFind:str='L'):
    shape = grid.shape
    if entityToFind == 'L':
        entityToFind = 2
    elif entityToFind == 'M':
        entityToFind = 1
    else:
        raise TypeError(f"EntityType {entityToFind} is not valid")

    for i in range(-shape[0],shape[0]): 
        if (mothPos[0]+i >= shape[0]) or (mothPos[0]+i < 0):
            continue

        for j in range(-shape[1],shape[1]):
            if (mothPos[1]+j >= shape[1]) or (mothPos[1]+j < 0):
                continue

            if (grid[tuple(mothPos + numpy.array([i,j]))] == entityToFind):
                return numpy.array([i,j])

#Returns ndarray(x,y) delta to move to the nearest light 
def findNextMove(grid:numpy.ndarray, mothPos:numpy.ndarray):
    deltaX, deltaY = 0,0
    lightRelPos = findClosestEntity(grid, mothPos,'L')
    #print(lightRelPos)
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
    
    return numpy.array([deltaX, deltaY])