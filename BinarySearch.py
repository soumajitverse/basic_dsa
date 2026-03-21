# for binary search array need to be sorted

def binS(arr, beg, end, x):

    if beg > end:
        return -1

    mid = (beg + end) // 2

    if x > arr[mid]:
        return binS(arr, mid + 1, end, x)

    elif x < arr[mid]:
        return binS(arr, beg, mid - 1, x)

    else:
        return mid


arr = list(map(int, input().split()))
n = int(input())

print(binS(arr, 0, len(arr) - 1, n))
