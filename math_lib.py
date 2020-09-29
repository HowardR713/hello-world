# Get the math library we need:
from decimal import *

class mymath:
    '''This is a docstring.  I have created a new class'''
    #---------------------------------------
    # Set the display value for the
    # current instance:
    #---------------------------------------
    def setDisplay(self):
        if self.mSign == 0:
            multiplier = 1
        else:
            multiplier = -1
        answer = multiplier * self.mInt * ( 10 ** self.mExp )
        fmt = '.' + str( abs( self.mExp ) ) + 'f'
        self.dispTerm1 = format( answer, fmt)

    #---------------------------------------
    # Return the display value for the
    # current instnace:
    #---------------------------------------
    def getDisplay(self):
        return self.dispTerm1
    
    #---------------------------------------
    # Constructor:  Creates a mymath object:
    #---------------------------------------
    def __init__(self, r1=0.0):
        # Original numbers:
        self.inputTerm1 = r1
        d1 = Decimal( self.inputTerm1 )
        self.mSign = d1.as_tuple().sign
        self.mExp = d1.as_tuple().exponent
        self.mInt = abs( int( d1 * ( 10 ** abs( self.mExp ) ) ) )
        self.setDisplay()

    #---------------------------------------
    # Show instance attributes:
    #---------------------------------------
    def dump(self):
        print( "Display:  [", self.getDisplay(), "]" )
        print( "Sign:     [", self.mSign, "]" )
        print( "Exponent: [", self.mExp, "]" )
        print( "Integer:  [", self.mInt, "]" )

    #---------------------------------------
    # Given a sign value return a sign multiplier:
    # if 0 ==> 1, if 1 == -1
    #---------------------------------------
    def getSign( self ):
        if self.mSign == 0:
            multiplier = 1
        else:
            multiplier = -1
        return multiplier

    #---------------------------------------
    # Given a sign value, input as an argument, 
    # return a sign multiplier:  Given 0, return 1; 
    # given 1, return -1
    #---------------------------------------
    def getInptSign( self, inptSign ):
        if inptSign == 0:
            multiplier = 1
        else:
            multiplier = -1
        return multiplier

    #---------------------------------------
    # Get the larger exponent of 2 numbers,
    # that of the current instance and the
    # exponent passed in:
    #---------------------------------------
    def getBiggestExp(self, inptExp):
        if abs( self.mExp ) > abs( inptExp ):
            newExp = self.mExp
        else:
            newExp = inptExp
        return newExp

    #---------------------------------------
    # Add the input number to this (self's) number:
    #---------------------------------------
    def add(self, dInput2):
        # Create a common exponent for the 2 integers to
        # properly add:
        newExp = mymath.getBiggestExp(self,dInput2.mExp)

        # Convert current instance to signed integer:
        signIt = self.getSign()
        iTerm1 = signIt * self.mInt * ( 10 ** self.mExp )
        iTerm1 = int( iTerm1 * ( 10 ** abs( newExp ) ) )

        # Convert the input term to signed integer:
        signIt = self.getInptSign(dInput2.mSign)
        iTerm2 = signIt * dInput2.mInt * ( 10 ** dInput2.mExp )
        iTerm2 = int( iTerm2 * ( 10 ** abs( newExp ) ) )

        # Add the signed integers:
        answer = iTerm1 + iTerm2

        # Return the answer as a new instance:
        answer = answer * ( 10 ** newExp )
        fmt = '.' + str( abs( newExp ) ) + 'f'
        answer = format( answer, fmt)
        dAnswer = mymath( answer )
        return dAnswer

    #---------------------------------------
    # Subtract the input number to this (self's) number:
    #---------------------------------------
    def subtract(self, dInput2):
        # Create a common exponent for the 2 integers to
        # properly subtract:
        newExp = mymath.getBiggestExp(self,dInput2.mExp)

        # Convert current instance to signed integer:
        signIt = self.getSign()
        iTerm1 = signIt * self.mInt * ( 10 ** self.mExp )
        iTerm1 = int( iTerm1 * ( 10 ** abs( newExp ) ) )

        # Convert the input term to signed integer:
        signIt = self.getInptSign(dInput2.mSign)
        iTerm2 = signIt * dInput2.mInt * ( 10 ** dInput2.mExp )
        iTerm2 = int( iTerm2 * ( 10 ** abs( newExp ) ) )

        # Subtract the signed integers:
        answer = iTerm1 - iTerm2

        # Return the answer as a new instance:
        answer = answer * ( 10 ** newExp )
        fmt = '.' + str( abs( newExp ) ) + 'f'
        answer = format( answer, fmt)
        dAnswer = mymath( answer )
        return dAnswer
    
    #---------------------------------------
    # Multiply the input number by this (self's) number:
    #---------------------------------------
    def multiply(self, dInput2):
        # Create a common exponent for the 2 integers to
        # properly multiply:
        newExp = self.mExp + dInput2.mExp

        # Convert current instance to signed integer:
        signIt = self.getSign()
        iTerm1 = signIt * self.mInt

        # Convert the input term to signed integer:
        signIt = self.getInptSign(dInput2.mSign)
        iTerm2 = signIt * dInput2.mInt

        # Add the signed integers:
        answer = iTerm1 * iTerm2

        # Return the answer as a new instance:
        answer = answer * ( 10 ** newExp )
        fmt = '.' + str( abs( newExp ) ) + 'f'
        answer = format( answer, fmt)
        dAnswer = mymath( answer )
        return dAnswer

    #---------------------------------------
    # Divide this number by the input number:
    #---------------------------------------
    def divide(self, dInput2):
        # Create a common exponent for the 2 integers to
        # properly multiply:
        newExp = self.mExp - dInput2.mExp

        # Convert current instance to signed integer:
        signIt = self.getSign()
        iTerm1 = signIt * self.mInt

        # Convert the input term to signed integer:
        signIt = self.getInptSign(dInput2.mSign)
        iTerm2 = signIt * dInput2.mInt

        # Add the signed integers:
        answer = iTerm1 / iTerm2

        # Return the answer as a new instance:
        answer = answer * ( 10 ** newExp )
        fmt = '.' + str( abs( newExp ) ) + 'f'
        answer = format( answer, fmt)
        dAnswer = mymath( answer )
        return dAnswer
