import numpy as np
import matplotlib.pyplot as plt

def ComplexArg(ArgAngle, ArgX, ArgY):
    axes = plt.subplot()

    gradient = np.tan(ArgAngle*np.pi)
    #finds the gradient of the argument
        #given that the tangent to the angle is m in the form y - y1 = m(x-x1)

    x = np.linspace(ArgX, 50, 1000)
    #range of x values to be plotted
    y = gradient*(x-ArgX)+ArgY
    #the function of the graph given in the formm y - y1 = m(x-x1), rearranged to give y as a variable 

    axes.set_aspect( 1 )
    #set axis to be square so that the line is not distorted
    plt.plot(x, y)
