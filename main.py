import numpy
from matplotlib import pyplot, colors

#  _._     _,-'""`-._
# (,-.`._,'(       |\`-/|
#     `-.-' \ )-`( , o o)
#           `-    \`_`"'- meow

# Empty =  0
# Moth  =  1
# Light =  2

import moth
#import rules
#import lights

class c_Grid:
    def __init__(self, grid:numpy.array, colorset:list=['#000000','#FF0000','#0000FF']):
        # black = nothing
        # red - moths
        # blue = light
        self._Index = 0
        self._InitialState = grid
        self._CurrentState = self._InitialState
        self._ColorSet = colors.ListedColormap(colorset)

    def display(self, show_plot:bool=False):
        print(self._CurrentState)
        if show_plot == True:
            fig,ax1 = pyplot.subplots(nrows=1,ncols=1)
            ax1.pcolor(self._CurrentState, cmap=self._ColorSet, edgecolor='#000000', alpha=0.7)
            fig.savefig(f"./out/graph_{self._Index}", bbox_inches='tight', pad_inches=0.02)
            pyplot.close()

    def update(self):
        tempState = self._CurrentState
        #Iterating thru every pos
        
        for i in range(tempState.shape[0]):
            for j in range(tempState.shape[1]):
                pass

        tempState += 1
        self._CurrentState = tempState
        self._Index += 1
        self.display(show_plot=True)

MyGrid = c_Grid(numpy.random.choice([0,1, 2],(60,60),p=[0.965, 0.025, 0.010]))

MyGrid.display(show_plot=True)
for i in range(5):
    MyGrid.update()

def plotDynamics(data):
    fig, axes = pyplot.subplots(figsize=(7, 6))
    axes.plot(data[0], data[2], label='moths', color='blue')  # Plot the moth population over time
    axes.plot(data[0], data[3], label='lights', color='red')  # Plot the light population over time
    axes.set_xlabel('Time (months)')  # Label the x-axis
    axes.set_ylabel('Number of individuals')  # Label the y-axis
    axes.legend(bbox_to_anchor=(.3, 1), fontsize=13, fancybox=False, shadow=False, frameon=False)  # Add a legend
    pyplot.savefig('temporalDynamics.pdf', bbox_inches='tight', pad_inches=0.02)  # Save the temporal dynamics as a PDF
    pyplot.close()  # Close the plot to free memory