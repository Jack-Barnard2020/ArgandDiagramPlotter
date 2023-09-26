import numpy as np
import matplotlib.pyplot as plt

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