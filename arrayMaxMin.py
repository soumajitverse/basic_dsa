# input: 1 2 3 4 5 6 7
# output: 7 1 6 2 5 3 4

arr = list(map(int, input().split()))

resArr = []

i = 0
j = len(arr) - 1

while(i < j):
    resArr.append(arr[j])
    resArr.append(arr[i])
    i += 1
    j -= 1
if i == j:
    resArr.append(arr[i])

for x in resArr:
    print(x, end=" ")
    