import matplotlib.pyplot as plt
import numpy as np



def ComplexNumber(RealPart, ComplexPart):
    plt.xlim(-((np.absolute(RealPart))+5), np.absolute(RealPart)+5)
    plt.ylim(-((np.absolute(ComplexPart))+5), np.absolute(ComplexPart)+5)
    #limits x and y view to +/- 5 from point

    plt.plot(RealPart, ComplexPart, marker="o", markersize=20)
    #plots point on grid

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

def ComplexAbsloute(XCordinate, YCordinate, Radius):
    figure, axes = plt.subplots()
    #Sets axis to a subplot so that circle can be overlayed
    Drawing_uncolored_circle = plt.Circle( (XCordinate, YCordinate ),
                                        Radius ,
                                        fill = False )
    #uses infomation from main.py to plot an unfilled circle
    
    axes.set_aspect( 1 )
    #sets axis to be in same divsions so shape isnt distorted
    axes.add_artist( Drawing_uncolored_circle )
    #adds circle to plot
    plt.xlim(-((np.absolute(XCordinate))+Radius+10), np.absolute(XCordinate)+Radius+10)
    plt.ylim(-((np.absolute(YCordinate))+Radius+10), np.absolute(YCordinate)+Radius+10)
    #limits x and y view to a sensible size given radius 

def Plot():
    plt.xlabel('Real', fontsize=20)
    #labe;s x axis as the real axis
    plt.ylabel('Imaginary', fontsize=20)
    #labels y axis as the imaginary axis
    plt.title("Argand Diagram", fontsize=20)
    #names the plot
    plt.grid()
    plt.show()

