import numpy
from matplotlib import pyplot, colors

#  _._     _,-'""`-._
# (,-.`._,'(       |\`-/|
#     `-.-' \ )-`( , o o)
#           `-    \`_`"'- meow

class c_Grid:
    def __init__(self, grid:numpy.array, colorset:list=['#FF0000','#00FF00','#0000FF']):
        self._Index = 0
        self._InitialState = grid
        self._CurrentState = self._InitialState
        self._ColorSet = colors.ListedColormap(colorset)

    def display(self, show_plot:bool=False):
        print(self._CurrentState)
        if show_plot == True:
            fig,ax1 = pyplot.subplots(nrows=1,ncols=1)
            ax1.pcolor(self._CurrentState, cmap=self._ColorSet, edgecolor='#000000', alpha=0.5)
            fig.savefig(f"./out/graph_{self._Index}")

    def update(self):
        tempState = self._CurrentState
        
        #Iterating thru every pos
        
        for i in range(tempState.shape[0]):
            for j in range(tempState.shape[1]):
                print(i,j)

        tempState += 1
        self._CurrentState = tempState

MyGrid = c_Grid(numpy.random.randint(0,3,(30,30)))

MyGrid.display(show_plot=True)
MyGrid.update()
print()
MyGrid.display()