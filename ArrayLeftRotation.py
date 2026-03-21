arr = list(map(int, input().split()))
d = int(input())

n = len(arr)
k = d % n

temp = []
for i in range(0, k):
    temp.append(arr[i])

for i in range(k, n): 
    arr[i - k] = arr[i]

j = 0
for i in range(n - k, n):
    arr[i] = temp[j]
    j += 1

for x in arr:
    print(x, end=" ")