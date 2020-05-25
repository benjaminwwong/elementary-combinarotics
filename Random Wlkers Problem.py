import math


#Random Walkers problem
pascallist = []
def sslist(li):# the term SigmaC**2 operates on the binomial expansion coefficients
    total = 0
    for num in li:
        total+=num**2
    return total
def prob(n):
    total = 0
    plist = []
    for num in range(n+1):
        total += (math.factorial(n)/(math.factorial(n-num)*math.factorial(num)))**2
    total = total/(4**n)
    return total

def proba(n):
    total = 0
    plist = []
    for num in range(n+1):
        total += (math.factorial(n)/(math.factorial(n-num)*math.factorial(num)))**2
    #total = total/(4**n)
    plist.append(total)
    plist.append(4**n)
    return plist


N = 0
while True:
    print(proba(N),N)
    N+=1

N=0
while True:
    print(prob(N))
    N += 1
           
