from math import pi
n = float(input('n = '))
r = 1
s = 0
while s != pi**2/6:
    s = s + 1/r**n
    r = r+1
    print (s)
