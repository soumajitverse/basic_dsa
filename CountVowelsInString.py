str = input()

str = str.lower()
vowel_count = 0

for x in str:
    if(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        vowel_count += 1

print(vowel_count)