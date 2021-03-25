import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import pandas as pd
# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    data_set1= pd.read_csv('ecg1.csv')
    x=data_set1.iloc[2*int(((i-100)+abs(i-100))/2):2*i,0].values
    y=data_set1.iloc[2*int(((i-100)+abs(i-100))/2):2*i,1].values
    plt.cla()
    axes = plt.gca()
    axes.plot(x, y, label='Channel 1')
    plt.legend(loc='upper left')
    plt.tight_layout()
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourc
plt.show()