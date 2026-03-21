r = int(input("enter row: "))
c = int(input("enter col: "))

mat1 = []
mat2 = []
result = []

print("enter 1st matrix:")
for i in range(r):
    row = list(map(int, input().split()))
    mat1.append(row)

print("enter 2nd matrix:")
for i in range(r):
    row = list(map(int, input().split()))
    mat2.append(row)

for i in range(r):
    row = []
    for j in range(c):
        row.append(mat1[i][j] + mat2[i][j])
    result.append(row)

print("result is:")
for i in range(r):
    for j in range(c):
        print(result[i][j], end=" ")
    print()