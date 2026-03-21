arr = list(map(int, input().split()))

sum = 0

for i in range(0, len(arr)):
    sum += arr[i]

print(sum)