def revNo(n):
    rev = 0 
    temp = n

    while(temp != 0):
        rev = (rev * 10) + (temp % 10)
        temp = temp // 10

    return rev

n = int(input())

if(n == revNo(n)):
    print("palindrome")
else:
    print("not palindrome")