import numpy as np
import matplotlib.pyplot as plt

def ComplexNumber(RealPart, ComplexPart):
    plt.xlim(-((np.absolute(RealPart))+5), np.absolute(RealPart)+5)
    plt.ylim(-((np.absolute(ComplexPart))+5), np.absolute(ComplexPart)+5)
    #limits x and y view to +/- 5 from point

    plt.plot(RealPart, ComplexPart, marker="o", markersize=20)
    #plots point on grid