def calGCD(a, b):
    if (a == 0 or b == 0):
        return "can't calculate"

    res = min(a, b)
    while res >= 1:
        if(a % res == 0 and b % res == 0):
            return res
        res -= 1
    return 1

a = int(input())
b = int(input())

print(calGCD(a, b))
