# Get the decimal libs:
import math_lib

def mathify( d1 ):
    mSign = d1.mSign
    mExp = d1.mExp
    mInt = d1.mInt
    mathTuple = ( mSign, mInt, mExp )
    return mathTuple

# Get input numbers:
s1 = "-6543.21"
t1 = "42"

# Process everything:
d1 = math_lib.mymath( s1 )
d2 = math_lib.mymath( t1 )

# Process s1:

# Print out everything:
print("=======================")
print("Hello world!")
mTuple = mathify( d1 )
print( d1.getDisplay() )
print( "sign", mTuple[0] )
print( "integer", mTuple[1] )
print( "exponent", mTuple[2] )

print("-----------------------")
mTuple = mathify( d2 )
print(d2.getDisplay())
print( "sign", mTuple[0] )
print( "integer", mTuple[1] )
print( "exponent", mTuple[2] )
print("-----------------------")

# Let's try some math:
print("adding two numbers:")
print( d1.getDisplay() )
s2 = '.123'
print( s2 )
d3 = d1.add( s2 )
mTuple = mathify( d3 )
print( "sign", mTuple[0] )
print( "integer", mTuple[1] )
print( "exponent", mTuple[2] )
print ("goodbye world!")
print("=======================")

