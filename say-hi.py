# Get the decimal libs:
from decimal import *

def mathify( sInput ):
    d1 = Decimal( sInput )
    mSign = d1.as_tuple().sign
    mExp = d1.as_tuple().exponent
    mInt = abs( int( d1 * ( 10 ** abs( mExp ) ) ) )
    mathTuple = ( mSign, mInt, mExp )
    return mathTuple

# Get input numbers:
s1 = "-6543.21"
t1 = "42"

# Process s1:

# Print out everything:
print("=======================")
print("Hello world!")
mTuple = mathify( s1 )
print( s1 )
print( "sign", mTuple[0] )
print( "integer", mTuple[1] )
print( "exponent", mTuple[2] )

print("-----------------------")
mTuple = mathify( t1 )
print(t1)
print( "sign", mTuple[0] )
print( "integer", mTuple[1] )
print( "exponent", mTuple[2] )
print ("goodbye world!")
print("=======================")

