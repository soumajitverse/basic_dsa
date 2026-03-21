def factN(n):
    if(n==0 or n==1):
        return 1
    return n * factN(n-1)

n = int(input(""))

print(factN(n))