def isValidAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
        
    freqMap = {}
    for x in str1:
        freqMap[x] = freqMap.get(x, 0) + 1
        
    for x in str2:
        if x not in freqMap:
            return False
        freqMap[x] -= 1
        if freqMap[x] < 0:
            return False
    return True

str1 = input()
str2 = input()

if(isValidAnagram(str1, str2)):
    print("Valid anagram")
else:
    print("not valid anagram")