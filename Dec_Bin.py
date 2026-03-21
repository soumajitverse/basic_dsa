n = int(input("enter no. in decimal:"))

if n == 0:
    print("binary value is:", 0)

else:
    temp = n
    res = 0
    c = 0

    while(temp != 0):
        rem = temp % 2
        res += rem * (10 ** c)
        c += 1
        temp //= 2

    print("binary value is:", res)