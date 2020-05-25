def ackermann(x,y):
    if x == 0:
        return y + 1
    elif y == 0:
        return ackermann(x-1,1)
    else:
        return ackermann(x-1,ackermann(x,y-1))

for x in range(10):
    for y in range(10):
        print(ackermann(x,y),x,y)
