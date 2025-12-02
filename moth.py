import numpy
import math
import random

### Rules
def tryDeath(grid:numpy.ndarray, mothPos:numpy.ndarray ):
    lightDist = findClosestEntity(grid, mothPos, entityToFind ='L')
    if math.sqrt((lightDist[0])**2 + lightDist[1]**2) <= 2:
        grid[mothPos[0],mothPos[1]] = 0
        return 0
    else:
        if math.sqrt((lightDist[0])**2 + lightDist[1]**2) <= random.randint(1,25):
            grid[mothPos[0],mothPos[1]] = 0
        return 1

def tryBirth(grid:numpy.ndarray, mothPos:numpy.ndarray):
    mothDist = findClosestEntity(grid, mothPos, entityToFind = 'M')
    if math.sqrt((mothDist[0])**2 + mothDist[1]**2) >=2:
        # find a nearby 0 and replace it to be a 1 somehow

        # Maybe use this function to find the 0 and turn it into a 1?
        emptyDist = findClosestEntity(grid, mothPos, entityToFind = "E" )
        r = random.random()
        # need to modify to have a probability dependent on the # of moths nearby
        if r <= 0.14:
            grid[mothPos[0]+emptyDist[0],mothPos[1]+emptyDist[1]] = 1
        pass
    if math.sqrt((mothDist[0])**2 + mothDist[1]**2) <2:
        return 2

### Movement
def _Move(grid:numpy.ndarray, mothPos:numpy.ndarray, mothDeltaPos:numpy.ndarray):
    try:
        # Move only if desired square is empty
        if (grid[tuple(mothPos+mothDeltaPos)] == 0):
            grid[tuple(mothPos+mothDeltaPos)] = 1
            grid[tuple(mothPos)] = 0
            return 1
        else:
            return 0
            #print(f"Cannot move moth: Space already taken by light or moth")
            pass
    except IndexError:
        #print(f"Cannot move moth: OOR ")
        return 0
        pass

def tryMovement(grid:numpy.ndarray, mothPos:numpy.ndarray):
    desired_Move = findNextMove(grid, mothPos)
    if not(_Move(grid, mothPos, desired_Move)):
        #print("Cannot Move to desired space, finding nearest empty space")
        dEmpty = findClosestEntity(grid=grid, mothPos=mothPos+desired_Move, entityToFind="E")
        _Move(grid, mothPos, desired_Move+dEmpty)


#Returns ndarray(x,y) delta to the nearest light 
def findClosestEntity(grid:numpy.ndarray, mothPos:numpy.ndarray, entityToFind:str='L'):
    # Create shape for local use, determine which grid value to check for given input
    
    gridShape = grid.shape
    maxDistance = 35
    searchShape = (maxDistance,maxDistance)

    if entityToFind == 'L':
        entityToFind = 2
    elif entityToFind == 'M':
        entityToFind = 1
    elif entityToFind == 'E':
        entityToFind = 0
    else:
        raise TypeError(f"EntityType {entityToFind} is not valid")
    
    closestLoc = tuple([10000,10000])   # Setup initial closest delta
    for i in range(-searchShape[0],searchShape[0]):     # For every row

        if (mothPos[0]+i >=gridShape[0]) or (mothPos[0]+i < 0): # with valid range
            continue

        for j in range(-searchShape[1],searchShape[1]):     # for every column 
            if (mothPos[1]+j >= gridShape[1]) or (mothPos[1]+j < 0):     # with valid range
                continue
            # If gridvalue is equal to desired value, and is closer than our current closest delta
            if ((grid[tuple(mothPos + numpy.array([i,j]))] == entityToFind) and ((math.sqrt((i**2 + j**2) < math.sqrt(closestLoc[0]**2 + closestLoc[1]**2) )))):
                closestLoc = tuple([i,j])   # setup new closest delta, conitnue to next possible square
    if closestLoc == tuple([10000,10000]):
        closestLoc = tuple([gridShape[0]//2,gridShape[1]//2])
    return closestLoc


#Returns ndarray(x,y) delta to move to the nearest light 
def findNextMove(grid:numpy.ndarray, mothPos:numpy.ndarray):
    deltaX, deltaY = 0,0
    lightRelPos = findClosestEntity(grid, mothPos,'L')  # Find delta to closest light
    #print(lightRelPos)
    max_movement = 3 # Change according to total size
    
    factorX = -1 if lightRelPos[0] < 0 else 1   #Setup directionality values
    factorY = -1 if lightRelPos[1] < 0 else 1   #
    
    deltaX = abs(lightRelPos[0])    # Normalize to magnitudes
    deltaY = abs(lightRelPos[1])    #

    # Setup distances
    if (abs(deltaX) >= max_movement):
        deltaX = round(max_movement * factorX)
    else:
        deltaX = round(deltaX*factorX)

    if (abs(deltaY) >= max_movement):
        deltaY = round(max_movement * factorY)
    else:
        deltaY = round(deltaY*factorY)
    #

    #Setup random deviation in moth movement
    max_deviation = max_movement//2

    deltaX += int(numpy.random.randint(-max_deviation,max_deviation,1))
    deltaY += int(numpy.random.randint(-max_deviation,max_deviation,1))

    baseMove = numpy.array([deltaX, deltaY], dtype=float)

    #Rotation - The way moths move in real life

    #Define rotationAngle, 0 is a straight line, 1 is a complete circle, minimal approach to point
    rotationAngle = 0.75   # Radians

    #Rotation Matrix - https://en.wikipedia.org/wiki/Rotation_matrix
    # rotation in xy-plane by desired rotation angle
    rotationMatrix = numpy.array([
        [numpy.cos(rotationAngle), -numpy.sin(rotationAngle)],
        [numpy.sin(rotationAngle),  numpy.cos(rotationAngle)]
    ])
    # Rotating baseMove
    spiralMoveMatrix = rotationMatrix @ baseMove

    #typecast to int, necessary for array movemnt
    finalMove = numpy.rint(spiralMoveMatrix).astype(int)

    return finalMove