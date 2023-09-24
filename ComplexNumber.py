import numpy as np
import matplotlib.pyplot as plt

def ComplexNumber():
    x = float(input("Input Real Part "))
    y = float(input("Input Complex Part "))

    plt.xlim(-((np.absolute(x))+5), np.absolute(x)+5)
    plt.ylim(-((np.absolute(y))+5), np.absolute(y)+5)
    #limits x and y view to +/- from point

    plt.plot(x, y, marker="o", markersize=20)
    #plots point on grid