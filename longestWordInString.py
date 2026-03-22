s = input()
words = s.split()
longestWord = words[0]
for word in words:
    if len(word) > len(longestWord):
        longestWord = word

print(longestWord)