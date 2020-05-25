n = 0
def check(n):
    req = len(str(n))
    num = str(n**n)
    num = num[0:req]
    #print(num,n,"Test")
    if int(num) == n:
        print(n,"True")
while True:
    check(n)
    n +=1
