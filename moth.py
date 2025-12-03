import numpy
import math
import random

ENVIRONMENT = "URBAN"   # "URBAN" or "RURAL"

if ENVIRONMENT == "RURAL":
    BIRTH_PROB = 0.25
    NATURAL_DEATH = 0.01
    
    # Light effect = LIGHT_BOOST / (dist^2 + 1)
    LIGHT_MORTALITY_BOOST = 0.70   # rural lights less harmful

elif ENVIRONMENT == "URBAN":
    BIRTH_PROB = 0.24
    NATURAL_DEATH = 0.012
    
    # Urban lights more dangerous — higher numerator
    LIGHT_MORTALITY_BOOST = 1.20

def tryDeath(grid:numpy.ndarray, gridnew:numpy.ndarray, mothPos:numpy.ndarray):

    # Distance to nearest light
    lightDist = findClosestEntity(grid, mothPos, entityToFind='L')
    dist = math.sqrt(lightDist[0]**2 + lightDist[1]**2)

    # Smoothly decaying mortality:
    # death = natural + light_effect(dist)
    death_prob = NATURAL_DEATH + (LIGHT_MORTALITY_BOOST / (dist**2 + 1))

    # Hard cap to avoid > 99% death at distance 0
    death_prob = min(death_prob, 0.85)

    if random.random() <= death_prob:
        gridnew[mothPos[0], mothPos[1]] = 0
        return 0

    return 1


def tryBirth(grid:numpy.ndarray, gridnew:numpy.ndarray, mothPos:numpy.ndarray):
    mothDist = findClosestEntity(grid, mothPos, entityToFind='M')
    dist = math.sqrt(mothDist[0]**2 + mothDist[1]**2)

    if dist >= 2:
        emptyDist = findClosestEntity(gridnew, mothPos, entityToFind="E")
        if random.random() <= BIRTH_PROB:
            newx = mothPos[0] + emptyDist[0]
            newy = mothPos[1] + emptyDist[1]
            gridnew[newx, newy] = 1

    return 2 if dist < 2 else 1

def _Move(grid:numpy.ndarray, gridnew:numpy.ndarray, mothPos:numpy.ndarray, mothDeltaPos:numpy.ndarray):
    try:
        target = tuple(mothPos + mothDeltaPos)
        if gridnew[target] == 0:
            gridnew[target] = 1
            grid[mothPos[0], mothPos[1]] = 0
            return 1
        return 0
    except IndexError:
        return 0


def tryMovement(grid:numpy.ndarray, gridnew:numpy.ndarray, mothPos:numpy.ndarray):
    desired_Move = findNextMove(grid, mothPos)
    if not _Move(grid, gridnew, mothPos, desired_Move):
        dEmpty = findClosestEntity(gridnew, mothPos + desired_Move, entityToFind="E")
        _Move(grid, gridnew, mothPos, desired_Move + dEmpty)


def findClosestEntity(grid:numpy.ndarray, mothPos:numpy.ndarray, entityToFind:str='L'):

    gridShape = grid.shape
    maxDistance = 35

    if entityToFind == 'L': target = 2
    elif entityToFind == 'M': target = 1
    elif entityToFind == 'E': target = 0
    else:
        raise TypeError(f"EntityType {entityToFind} is not valid")

    closest = (10000, 10000)

    for i in range(-maxDistance, maxDistance):
        for j in range(-maxDistance, maxDistance):

            x = mothPos[0] + i
            y = mothPos[1] + j

            if x < 0 or x >= gridShape[0] or y < 0 or y >= gridShape[1]:
                continue

            if grid[x, y] == target:
                if (i*i + j*j) < (closest[0]*closest[0] + closest[1]*closest[1]):
                    closest = (i, j)

    if closest == (10000, 10000):
        return (gridShape[0]//2, gridShape[1]//2)

    return closest


def findNextMove(grid:numpy.ndarray, mothPos:numpy.ndarray):

    lightRelPos = findClosestEntity(grid, mothPos, 'L')
    max_movement = 3

    factorX = -1 if lightRelPos[0] < 0 else 1
    factorY = -1 if lightRelPos[1] < 0 else 1

    deltaX = min(abs(lightRelPos[0]), max_movement) * factorX
    deltaY = min(abs(lightRelPos[1]), max_movement) * factorY

    max_deviation = max_movement // 2
    deltaX += random.randint(-max_deviation, max_deviation)
    deltaY += random.randint(-max_deviation, max_deviation)

    baseMove = numpy.array([deltaX, deltaY], dtype=float)

    rotationAngle = 0.75
    rotationMatrix = numpy.array([
        [numpy.cos(rotationAngle), -numpy.sin(rotationAngle)],
        [numpy.sin(rotationAngle),  numpy.cos(rotationAngle)]
    ])

    finalMove = rotationMatrix @ baseMove
    return numpy.rint(finalMove).astype(int)
