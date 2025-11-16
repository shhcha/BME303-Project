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
            ax1.pcolor(self._CurrentState, cmap=self._ColorSet, edgecolor='#000000', alpha=0.7)
            ax1.set_title(f"ITER:{self._Index}")
            ax1.set_xlabel("X Pos")
            ax1.set_ylabel("Y Pos")
            fig.savefig(f"./out/graph_{self._Index}", bbox_inches='tight', pad_inches=0.2)
            pyplot.close()

    def update(self):
        newState = self._CurrentState.copy()
        #Iterating thru every pos
        
        rules.update(self._CurrentState, newState)

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



### Start Running
numpy.random.seed(0)

MyGrid = c_Grid(numpy.random.choice([0,1, 2],(120,120),p=[0.965, 0.025, 0.010]))

MyGrid.display(show_plot=True)
for i in range(60):
    MyGrid.update()
create_gif()

def plotDynamics(data): #MOVE AWAY
    fig, axes = pyplot.subplots(figsize=(7, 6))
    axes.plot(data[0], data[2], label='moths', color='blue')  # Plot the moth population over time
    axes.plot(data[0], data[3], label='lights', color='red')  # Plot the light population over time
    axes.set_xlabel('Time (months)')  # Label the x-axis
    axes.set_ylabel('Number of individuals')  # Label the y-axis
    axes.legend(bbox_to_anchor=(.3, 1), fontsize=13, fancybox=False, shadow=False, frameon=False)  # Add a legend
    pyplot.savefig('temporalDynamics.pdf', bbox_inches='tight', pad_inches=0.02)  # Save the temporal dynamics as a PDF
    pyplot.close()  # Close the plot to free memory