import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("ecg1.csv", delimiter=",", names=["x", "y"])
def zoom(axis ,valueX , valueY):
    if axis == "x":
        plt.xscale('symlog',linthreshx = valueX)
    elif axis == "y":
        plt.yscale('symlog',linthreshy = valueY)
    elif axis == "x&y":
        plt.xscale('symlog',linthreshx = valueX)
        plt.yscale('symlog',linthreshy = valueY)
    else:
        print("You must Type 'x' or 'y' or 'x&y'")


zoom("x" ,0.1 ,5)
plt.plot(data['x'], data['y'])
plt.show()