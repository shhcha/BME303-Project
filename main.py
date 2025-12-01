import numpy
from matplotlib import pyplot, colors
import re

#  _._     _,-'""`-._
# (,-.`._,'(       |\`-/|
#     `-.-' \ )-`( , o o)
#           `-    \`_`"'- meow

# Empty =  0
# Moth  =  1
# Light =  2

import moth
import rules
#import lights

import imageio.v2 as imageio
import glob

class c_Grid: #Class of numpy array, with graph and update func
    def __init__(self, grid:numpy.array, colorset:list=['#000000','#FF0000','#0000FF']):
        # black = nothing
        # red - moths
        # blue = light
        self._Index = 0
        self._InitialState = grid
        self._CurrentState = self._InitialState
        self._ColorSet = colors.ListedColormap(colorset)

    def display(self, show_plot:bool=False):
        #print(self._CurrentState)
        if show_plot == True:
            fig,ax1 = pyplot.subplots(nrows=1,ncols=1, figsize=(16,9))
            g = ax1.pcolor(self._CurrentState, cmap=self._ColorSet, edgecolor='#000000', alpha=0.7)
            cbar = fig.colorbar(g, ax=ax1, label="", ticks=[0.3333, 1, 1.666])
            cbar.ax.set_yticklabels(["Empty", "Moth", "Light"])
            ax1.set_title(f"Week:{self._Index}")
            ax1.set_xlabel("X Pos (.1 miles)")
            ax1.set_ylabel("Y Pos (.1 miles)")
            fig.savefig(f"./out/graph_{self._Index}", bbox_inches='tight', pad_inches=0.2)
            pyplot.close()
    

    def update(self, dataPool:numpy.ndarray):
        newState = self._CurrentState.copy()    # Setup new data

        dP = rules.update(self._CurrentState, newState)
        #print(f"returned: {dP}")
        dataPool[0][self._Index] = self._Index
        dataPool[1][self._Index] = dP[0]
        dataPool[2][self._Index] = dP[1]
        dataPool[3][self._Index] = dP[2]
        
        #print(dataPool)

        self._CurrentState = newState
        self._Index += 1
        self.display(show_plot=True)

def numerical_sort_key(s):
    # Splits the string into a list of number and non-number parts
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

def create_gif():
    # gather all plots, sort by file name using the numerical key
    plots = sorted(glob.glob("out/graph_**.png"), key=numerical_sort_key) # <-- FIX IS HERE

    # read and compile into a GIF
    images = [imageio.imread(p) for p in plots]
    imageio.mimsave('out/graphs.gif', images, fps=5)

def plotDynamics(data):
    
    fig, axes = pyplot.subplots(figsize=(7, 6))
    axes.plot(data[0], data[2], label='moths', color='red')  # Plot the moth population over time
    axes.plot(data[0], data[3], label='lights', color='blue')  # Plot the light population over time
    axes.set_xlabel('Time (Weeks)')  # Label the x-axis
    axes.set_ylabel('Number of Individuals')  # Label the y-axis
    axes.legend(bbox_to_anchor=(.3, 1), fontsize=13, fancybox=False, shadow=False, frameon=False)  # Add a legend
    pyplot.savefig('out/temporalDynamics.png', bbox_inches='tight', pad_inches=0.02)  # Save the temporal dynamics as a PDF
    pyplot.close()  # Close the plot to free memory


mothSpawn = 0.15
lightSpawn = 0.002

MyGrid = c_Grid(numpy.random.choice([0,1, 2],(100,100),p=[(1-(mothSpawn+lightSpawn)), mothSpawn, lightSpawn]))

MyGrid.display(show_plot=True)
iterations = 100
dynamics = numpy.zeros((4,iterations))

for i in range(iterations):
    print(f"Starting Frame{i+1}")
    MyGrid.update(dataPool=dynamics)

create_gif()
plotDynamics(dynamics)

