arr = list(map(int, input().split()))

# by in built function
# arr.reverse()

# by slice in reverse order
# arr = arr[::-1]

i = 0
j = len(arr) - 1

while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1


for x in arr:
    print(x, end = " ")