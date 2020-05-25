#Gives the coefficients of any number in decimal form
from math import e
from math import pi
from math import floor
def cont(x):
    print (x)
    print (floor(x))
    if x > 0 :
        while x != 0:
            x = 1/(x - floor(x))
            if floor(x+1)-x<0.000000001 or x>100000000 :#helps eliminate common commputational errors
                x = floor(x+1)
                print("Warning: potential error")
            print (floor(x))


n = input("n?")
if n == "pi":
    n = pi
if n == "e":
    n = e
cont(float(n))

