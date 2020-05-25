from math import factorial
x = 0
d = input("e^x")
d = float(d)
r = 0
while True:
    r = r + d**x/factorial(x)
    x = x + 1
    print (r)
    
    
