n = int(input("enter binary number: "))

temp = n
res = 0
c = 0

while(temp != 0):
    rem = temp % 10
    res += rem * (2 ** c)
    c += 1
    temp //= 10

print("decimal value is:", res)