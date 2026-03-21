def linS(arr, n):
    for i in range (0, len(arr)):
        if arr[i] == n:
            print(i)
            return
    print("not found")
    return


arr = list(map(int, input().split()))
n = int(input())

linS(arr, n)

