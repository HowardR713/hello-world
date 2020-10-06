# Exercise the math library.  
# Get the decimal libs:
import math_lib

def execOps(op,t1,t2):
    # Set up some vars:
    isError = 0
    # Set up the terms:
    d1 = math_lib.mymath( t1 )
    d2 = math_lib.mymath( t2 )
    # Make decisions based on the operation:
    if (op=='+'):
        # Addition -> sum:
        msg = "Addition:"
        ansMsg = "Sum:"
        d3 = d1.add( d2 )
    elif (op=='-'):
        # Subtraction -> difference:
        msg = "Subtraction"
        ansMsg = "Difference:"
        d3 = d1.subtract( d2 )
    elif (op=="*"):
        # Multiplication -> product:
        msg = "Multiplication"
        ansMsg = "Product:"
        d3 = d1.multiply( d2 )
    elif (op=="/"):
        # Division -> quotient:
        msg = "Division"
        ansMsg = "Quotient:"
        if (d2.mInt==0):
            msg = "ERROR:  Can't divide by 0."
            isError = 1
        else:
            d3 = d1.divide( d2 )
    else:
        msg = "ERROR:  Invalid operation: "
        isError = 1
    if (isError==0):
        print( msg, "-----------------------")
        print("Term 1:  --------------")
        d1.dump()
        print("Term 2:  --------------")
        d2.dump()
        print( ansMsg, "-----------------------")
        d3.dump()
    else:
        print(ansMsg,op)
    print("-----------------------")

# Get input numbers:
t1 = "-6543.21"
t2 = "42.00001"

# Let's try some math.  Print out everything:
print("=======================")
print("Hello world!")
print("-----------------------")
# -----------------------
t1 = "-6543.21"
t2 = "42.00001"
execOps("+",t1,t2)
# -----------------------
t1 = "-6543.21"
t2 = "42.00001"
execOps("-",t1,t2)
# -----------------------
t1 = "-.000000000000000000015"
t2 = "0.000000000000000000115"
execOps("*",t1,t2)
# -----------------------
t1 = "8.104012345"
t2 = "5.0002"
execOps("/",t1,t2)
print ("goodbye world!")
print("=======================")
