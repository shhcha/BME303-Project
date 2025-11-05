import numpy
from matplotlib import pyplot

class c_Moth:
    pass
class c_Light:
    pass

class c_Grid:
    def __init__(self, grid:numpy.array):
        self._InitialState = grid
        self._CurrentState = self._InitialState

    def display(self):
        print(self._CurrentState)

    def update(self):
        tempState = self._CurrentState
        # Do something to tempState
        tempState += 1
        self._CurrentState = tempState

MyGrid = c_Grid(numpy.random.randint(0,3,(20,20)))

MyGrid.display()
MyGrid.update()
print()
MyGrid.display()