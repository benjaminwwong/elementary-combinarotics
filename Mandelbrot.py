def Mandelbrot():
    c = complex(float(input("Re:")),float(input("Im:")))
    li = []
    z = complex(0,0)
    while abs(z) < 2:
        z = z^2 + c
        if z in li:
            break
        li.append(z)
        print(z)
