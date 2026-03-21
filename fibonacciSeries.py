# this is for printing n terms of fibonacci series
def fiboSeries(n):
    a = 0 
    b = 1
    
    if(n==0):
        print("")
        return
    if(n==1):
        print(a)
        return
    if(n==2):
        print(a, b)
        return
    
    print(a, b, end=" ")
    for i in range(0, n-2):
        c = a + b
        a = b
        b = c
        print(c, end=" ")


# this for nth term of the fibonacci series
def fiboTerm(n):
    a = 0
    b = 1
    if(n==0):
        print("")
        return
    if(n==1):
        print(a)
        return
    if(n==2):
        print(b)
        return
    for i in range(0, n-2):
        c = a + b
        a = b
        b = c
    print(c)    


n = int(input())
fiboSeries(n)
print("")
fiboTerm(n)