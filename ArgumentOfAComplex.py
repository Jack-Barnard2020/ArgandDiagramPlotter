import numpy as np
import matplotlib.pyplot as plt

def ComplexArg():
    axes = plt.subplot()

    argAngle = (int(input("Numerator of Argument "))/int(input("Denominator of Argument ")))
    #finds the fractional value of pi

    argZx = float(input("real part" ))
    argZy = float(input("complex part "))
    #asks for the real and complex part of a discrete complex number
        #x is real
        #y is complex

    gradient = np.tan(argAngle*np.pi)
    #finds the gradient of the argument
        #given that the tangent to the angle is m in the form y - y1 = m(x-x1)

    x = np.linspace(argZx, 50, 1000)
    #range of x values to be plotted
    y = gradient*(x-argZx)+argZy
    #the function of the graph given in the formm y - y1 = m(x-x1), rearranged to give y as a variable 

    axes.set_aspect( 1 )
    #set axis to be square so that the line is not distorted

    return plt.plot(x, y)

#returns the action to be carried out