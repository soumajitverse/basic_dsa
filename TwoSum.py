# bruteforce approach
def twoSum1(nums, target):
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

# optimised approach
def twoSum2( nums, target):
        n = len(nums)
        hashMap = {}
        for i in range(n):
            hashMap[nums[i]] = i
        
        for i in range(n):
            needed = target - nums[i]
            if needed in hashMap and hashMap[needed] != i:
                return [i, hashMap[needed]]



arr = list(map(int, input().split()))
target = int(input())
print(twoSum2(arr, target))