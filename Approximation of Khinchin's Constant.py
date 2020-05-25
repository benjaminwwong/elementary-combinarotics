from math import floor
from math import pi
lisst = []
c = pi  
j = 1
p = 0
def cont(x):
    if x > 0 :
        if x != 0:
            x = 1/(x - floor(x))
            if floor(x+1)-x<0.000000001:#helps eliminate common commputational errors
                x = floor(x+1)
            lisst.append(floor(x))


while True:
    j=1
    cont(c)
    for d in lisst:
        j = j*d

    p = j**(1/len(lisst))
    c = 1/(c - floor(c))
    print (p)
    print (lisst)

    
        

