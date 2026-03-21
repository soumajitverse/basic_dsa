arr = list(map(int, input().split()))

max_ele = arr[0]

for i in range(0, len(arr)):
    if(max_ele < arr[i]):
        max_ele = arr[i]

print(max_ele)