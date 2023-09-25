import AbslouteOfAComplex as Absi
import ArgumentOfAComplex as Argi
import ComplexNumber as i
import matplotlib.pyplot as plt



def PlotComplexNumber():
    Real = float(input("Input the real part of a complex number? "))
    Complex = float(input("Input the complex part of a complex number? "))
    i.ComplexNumber(Real, Complex)

def PlotArgument():
    ArgAngle = int(input("Input numerator of fractional value of pi? "))/int(input("Input denominator of fractional value of pi? "))
    #asks for a fractional value of pi with out p, pi is multiplied onto value in ArgumentOFACOMplex
    
    ArgX = float(input("Input the real part of a complex number? "))
    ArgY = float(input("Input the complex part of a complex number? "))
    Argi.ComplexArg(ArgAngle, ArgX, ArgY)

def PlotAbslouteValue():
    CenterX = -float(input("real part? "))
    CenterY = -float(input("complex part? "))
    #opposite sign of the part will be the center

    Radius = float(input("absloute value? "))
    #radius is equal to the absloute value of a complex number, when plotted on an argand diagram

    Absi.ComplexAbsloute(CenterX, CenterY, Radius)

def Plot():
    plt.xlabel('Real', fontsize=20)
    #labe;s x axis as the real axis
    plt.ylabel('Imaginary', fontsize=20)
    #labels y axis as the imaginary axis
    plt.title("Argand Diagram", fontsize=20)
    #names the plot
    plt.grid()
    plt.show()



Plot()