def calLCM(a, b):
    if (a == 0 or b == 0):
        return "can't calculate"

    res = max(a, b)
    while(True):
        if(res % a == 0 and res % b == 0):
            return res
        res += 1

a = int(input())
b = int(input())

print(calLCM(a, b))