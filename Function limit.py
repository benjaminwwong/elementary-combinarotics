import math
def func(x):
    s = 0
    for n in range(x):
        s += 1/(math.sqrt(n+1)*math.sqrt(n+2))
    return s
q = 1
while True:
    print(func(q))
    q +=10000000
    
