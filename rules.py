import numpy as np
import moth
import math


def lights():
    pass



def dimming():
    pass
def mothMove():
    pass

def updateMoth(oldGrid:np.ndarray, newGrid:np.ndarray,x:int, y:int):
    #print(f"Updating Moth:{x}:{y}")
    moth.tryMovement(newGrid, np.array([x,y]))
    pass
def updateLight(oldGrid:np.ndarray, newGrid:np.ndarray,x:int, y:int):
    #print(f"Updating Light:{x}:{y}")
    pass
def updateEmpty(oldGrid:np.ndarray, newGrid:np.ndarray,x:int, y:int):
    #print(f"Updating Empty:{x}:{y}")
    return
    

def update(oldGrid:np.ndarray, newGrid:np.ndarray): #a function that checks what square it is, and calls the other functions accordingly, and returns dyanmics data
    count0, count1, count2 = 0,0,0
    # For row, column, check value and follow updaterules according to type
    for i in range(oldGrid.shape[0]):
            for j in range(oldGrid.shape[1]):
                if (oldGrid[i][j] == 0):
                    count0 += 1
                    updateEmpty(oldGrid=oldGrid, newGrid=newGrid, x=i,y=j)
                elif (oldGrid[i][j] == 1):
                    count1 += 1
                    updateMoth(oldGrid=oldGrid, newGrid=newGrid, x=i,y=j)
                elif (oldGrid[i][j] == 2):
                    count2 += 1
                    updateLight(oldGrid=oldGrid, newGrid=newGrid, x=i,y=j)
                else:
                    print(f"Wrong Value {i}:{j}")
    # Return counts (for dynamics)
    return (tuple([count0, count1, count2]))
    
    