str = input()

# by using pre-defined functions

# str = str.replace(" ","")

# str = "".join(str.split())

# without using any predefined functions
res = ""

for x in str:
    if x != " ":
        res += x


str = res

print(str)