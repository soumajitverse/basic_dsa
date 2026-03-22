def removeDuplicates(nums):
    i = 0
    n = len(nums)
    idx = 0

    while(i < n):
        item = nums[i]
        while i < n and item == nums[i]:
            i += 1
        nums[idx] = item
        idx += 1
    return idx
        
arr = list(map(int, input().split()))
k = removeDuplicates(arr)

for i in range(0, k):
    print(arr[i], end=" ")