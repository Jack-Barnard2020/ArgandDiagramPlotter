import Plotter as plot


running = True
AvalibleRunningOptions = ["y", "n"]
AvailbleMenuOptions = [1,2,3]
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

def menu():
    MenuOption = input("What would you like to do? \n   1. Draw an absloute value \n   2. Draw an argument \n   3. Plot a complex number ")
    try:
        MenuOption = int(MenuOption)
        if MenuOption in AvailbleMenuOptions:
                if MenuOption == 1:
                    PlotAbslouteValue()
                elif MenuOption == 2:
                    PlotArgument()
                elif MenuOption == 3:
                    PlotComplexNumber()
                else:
                    print('ERROR \nsomething else went wrong, please try again')
                    menu()
        else:
            print("ERROR \nnumber not in range, please try again")
            menu()
    except TypeError:
        print("ERROR \nYou have not inputted a number, please try again")
        menu()
    except ValueError:
        print("ERROR \nYou have not inputted a number, please try again")
        menu()

def run():
    running = True
    while running == True:
        menu()
        AnotherPlot = input("Would you like to plot another propery before we draw the graph? y/n? ")
        try:
            AnotherPlot = AnotherPlot.lower()
            if AnotherPlot in AvalibleRunningOptions:
                if AnotherPlot == "y":
                    running = True
                else:
                    running = False
            else:
                print("ERROR \n not a valid input, please try agin")
        except ValueError:
            print("ERROR \n Not a letter, please try again")



run()
plot.Plot()