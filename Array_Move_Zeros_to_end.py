arr = list(map(int, input().split()))
n = len(arr)
insert_position = 0

for i in range(0, n):
    if arr[i] != 0:
        arr[insert_position] = arr[i]
        insert_position += 1

for j in range(insert_position, n):
    arr[j] = 0

for x in arr:
    print(x, end=" ")
