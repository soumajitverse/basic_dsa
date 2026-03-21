str = input()

str = str.lower()
cons_count = 0

for x in str:
    if(x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u'):
        cons_count += 1


print(cons_count)