marks = [[8, 3, 4],
[1, 5, 9],
[6, 7, 2]
]
i=0
while i<len(marks):
    j=0
    column=0
    row=0
    daigonal=0
    l=len(marks[i])
    while j<l:
        row=row+marks[i][j]
        column=column+marks[j][i]
        daigonal=daigonal+marks[j][j]
        j+=1
    i+=1
print(column,"column")
print(row,"row")
print(daigonal,"daigonal")
print()
if row==column==daigonal:
    print("magic square")
else:
    print("not a magic square")


# magic_square = [
# [8, 3, 4],
# [1, 5, 9],
# [6, 7, 2]
# ]
# print ((magic_square[0]))
# print ((magic_square[1]))
# print ((magic_square[2]))
# print(magic_square[0][0])
# print(magic_square[1][1])
# print(magic_square[2][2])
# print(magic_square[0][2])
# print(magic_square[1][2])


