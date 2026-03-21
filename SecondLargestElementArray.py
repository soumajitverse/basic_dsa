arr = list(map(int, input().split()))
n = len(arr)
m1 = m2 = min(arr)

for i in range(n):
    if arr[i] > m1:
        m2 = m1
        m1 = arr[i]
    elif arr[i] > m2 and arr[i] != m1:
        m2 = arr[i]

print(m2)
        