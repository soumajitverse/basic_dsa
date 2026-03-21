arr = list(map(int, input().split()))
d = int(input())

n = len(arr)
k = d % n

temp = []
for i in range(n - k, n):
    temp.append(arr[i])

for i in range(n-1-k, -1, -1):
    arr[i + k] = arr[i]

j = 0
for i in range(0, k):
    arr[i] = temp[j]
    j += 1

for x in arr:
    print(x, end=" ")