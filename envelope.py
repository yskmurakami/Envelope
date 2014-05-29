from mpl_toolkits.axes_grid.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

n = 200 # define the number of lines

def f(x,a): # define the function, x as parameter 
    return -x**2+a*x

def subplots(): # learn by "http://matplotlib.org/examples/axes_grid/demo_axisline_style.html"
    
    fig = plt.figure(1)
    ax = SubplotZero(fig, 111)
    fig.add_subplot(ax)

    for direction in ["xzero", "yzero"]:# define the shape of axes
        ax.axis[direction].set_axisline_style("-|>")
        ax.axis[direction].set_visible(True)

    for direction in ["left", "right", "bottom", "top"]:# hide the ticks around the graph
        ax.axis[direction].set_visible(False)

    return fig, ax

fig, ax = subplots()  # call the local version, not plt.subplots()

plt.axis([-n**0.8, n**0.8, -n*0.02, n]) # the range of graph (xmin,xmax,ymin,ymax)

plt.xticks([0]) # plot the origin point on the x-axis
plt.yticks([]) # plot nothing on the y-axis

a = np.linspace(-2*n, 2*n, 100*n) # the range of each line (xmin,xmax,***)

for x in range(n):
    y = f(x-n/2+0.5, a)
    ax.plot(a, y, 'r-', linewidth=2) # draw lines
plt.show()