import Plotter as plot


running = True
Menu = [1,2,3]
MenuOption = int()
AnotherPlot = str()

def PlotComplexNumber():
    Real = float(input("Input the real part of a complex number? "))
    Complex = float(input("Input the complex part of a complex number? "))
    plot.ComplexNumber(Real, Complex)

def PlotArgument():
    ArgAngle = int(input("Input numerator of fractional value of pi? "))/int(input("Input denominator of fractional value of pi? "))
    #asks for a fractional value of pi with out p, pi is multiplied onto value in ArgumentOFACOMplex
    
    ArgX = float(input("Input the real part of a complex number? "))
    ArgY = float(input("Input the complex part of a complex number? "))
    plot.ComplexArg(ArgAngle, ArgX, ArgY)

def PlotAbslouteValue():
    CenterX = -float(input("real part? "))
    CenterY = -float(input("complex part? "))
    #opposite sign of the part will be the center

    Radius = float(input("absloute value? "))
    #radius is equal to the absloute value of a complex number, when plotted on an argand diagram

    plot.ComplexAbsloute(CenterX, CenterY, Radius)

