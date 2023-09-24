import numpy as np
import matplotlib.pyplot as plt

def ComplexNumber():
    x = float(input("Input Real Part "))
    y = float(input("Input Complex Part "))
    plt.xlim(-((np.absolute(x))+5), np.absolute(x)+5)
    plt.ylim(-((np.absolute(y))+5), np.absolute(y)+5)
    plt.plot(x, y, marker="o", markersize=20)