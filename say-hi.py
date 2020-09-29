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
t1 = "42.00001"

# Process everything:
d1 = math_lib.mymath( s1 )
d2 = math_lib.mymath( t1 )

# Let's try some math:
# Print out everything:
print("=======================")
print("Hello world!")
print("Adding the two numbers:")
d1.dump()
print("-----------------------")
d2.dump()
print("-----------------------")
d3 = d1.add( d2 )
d3.dump()
print("-----------------------")
print("Subtraction:")
d1.dump()
print("-----------------------")
d2.dump()
print("-----------------------")
d4 = d1.subtract( d2 )
d4.dump()
print("-----------------------")
print("Multiplication:")
s1 = "-300000000000000"
t1 = "0.0005"
d1 = math_lib.mymath( s1 )
d2 = math_lib.mymath( t1 )
d1.dump()
print("-----------------------")
d2.dump()
print("-----------------------")
d3 = d1.multiply( d2 )
d3.dump()
print("-----------------------")
print("Division:")
s1 = "208.104"
t1 = "5.2"
d1 = math_lib.mymath( s1 )
d2 = math_lib.mymath( t1 )
d1.dump()
print("-----------------------")
d2.dump()
print("-----------------------")
d3 = d1.divide( d2 )
d3.dump()
print("-----------------------")
print ("goodbye world!")
print("=======================")
