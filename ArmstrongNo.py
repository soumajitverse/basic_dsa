def isArmStrong(n):
    c = 0
    temp = n
    sum = 0
    while(temp != 0):
        temp = temp // 10
        c += 1
    temp = n
    while(temp != 0):
        sum +=( (temp % 10) ** c)
        temp = temp // 10

    return sum == n

n = int(input())

if(isArmStrong(n)):
    print("armstrong")
else:
    print("not armstrong")