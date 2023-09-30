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
    #sets point at which line will go from
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
    #asks for user input 
    try:
        MenuOption = int(MenuOption)
        #tries to make input an integer such that it can be prosseed by IFTT
        if MenuOption in AvailbleMenuOptions:
                #checks that input is in range
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
            #user doesn\t input 1,2,3 but is still a number
    except TypeError:
        print("ERROR \nYou have not inputted a number, please try again")
        menu()
    except ValueError:
        print("ERROR \nYou have not inputted a number, please try again")
        menu()
    #except errors print when an invalid input is, ie not a number

def anotherplot():
    AnotherPlot = input("Would you like to plot another propery before we draw the graph? y/n? ")
    #user input can break the while loop casuing the Argand Diagram to be plotted
    try:
        AnotherPlot = AnotherPlot.lower()
        #checks for a valid input then breaks or runs program acordingly
        if AnotherPlot in AvalibleRunningOptions:
            if AnotherPlot == "n":
                running = False
            elif AnotherPlot == "y":
                running = True
            else:
                print("ERROR \nSomething else went wrong, please try again")
                anotherplot()
        else:
                print("ERROR \nNot a valid input, please try agin")
                anotherplot()
    except ValueError:
        print("ERROR \nNot a letter, please try again")
        #fail prints when a number or symbol is inputed
        anotherplot()
    return running

def run():
    running = True
    while running == True:
        #infinite while loop
        menu()
        running = anotherplot()




run()
plot.Plot()