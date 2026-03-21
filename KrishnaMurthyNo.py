def factN(n):
    if(n==0 or n==1):
        return 1
    return n * factN(n-1)


def isKrihnaMurthy(n):
    sum = 0
    temp = n
    while(temp != 0):
        sum += factN(temp%10)
        temp = temp // 10

    return sum == n


n = int(input(""))

if (isKrihnaMurthy(n)):
    print("krishnamurthy no.")
else:
    print(" not krishnamurthy no.")