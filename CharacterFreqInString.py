str = input()

freqMap = {}

for ch in str:
    if ch not in freqMap:
        freqMap[ch] = 1
    else:
        freqMap[ch] += 1

for key in freqMap:
    print(key, "---", freqMap[key])