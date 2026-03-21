def primeCheck(n):
    if n <= 1:
        print("not prime")
        return
    
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            print("not prime")
            return

    print("prime")


n = int(input())
primeCheck(n)