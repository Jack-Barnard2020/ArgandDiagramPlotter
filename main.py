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
    ArgX = float(input("Input the real part of a complex number? "))
    ArgY = float(input("Input the complex part of a complex number? "))
    Argi.ComplexArg(ArgAngle, ArgX, ArgY)

def PlotAbslouteValue():
    CenterX = -float(input("real part? "))
    CenterY = -float(input("complex part? "))
    Radius = float(input("absloute value? "))
    Absi.ComplexAbsloute(CenterX, CenterY, Radius)



plt.grid()
plt.show()

