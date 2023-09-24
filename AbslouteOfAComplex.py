import numpy as np
import matplotlib.pyplot as plt

def ComplexAbsloute():
    x = -float(input("real part? "))
    y = -float(input("complex part? "))
    r = -float(input("absloute value? "))

    figur, axes = plt.subplots()
    Drawing_uncolored_circle = plt.Circle( (x, y ),
                                        r ,
                                        fill = False )
    
    axes.set_aspect(1)
    axes.add_artist( Drawing_uncolored_circle )
    plt.xlim(-((np.absolute(x))+r+10), np.absolute(x)+r+10)
    plt.ylim(-((np.absolute(y))+r+10), np.absolute(y)+r+10)