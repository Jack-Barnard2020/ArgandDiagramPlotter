import numpy as np
import matplotlib.pyplot as plt

def ComplexArg():
    axes = plt.subplot()
    argAngle = (int(input("Numerator of Argument "))/int(input("Denominator of Argument ")))
    argZx = float(input("real part" ))
    argZy = float(input("complex part "))
    gradient = np.tan(argAngle*np.pi)
    x = np.linspace(argZx, 50, 1000)

    y = gradient*(x-argZx)-argZy
    axes.set_aspect( 1 )
    return plt.plot(x, y)