
##TABLE 5
###25,13,1,19,7
###16,9,22,15,3
###12,5,18,6,24
###8,21 14 2 20
###4,17,10,23,11

a=[]
i=0
while i<5:
    b=[]
    b.append(int(input("enter1:")))
    b.append(int(input("enter 2")))
    b.append(int(input("enter3")))
    b.append(int(input("enter4")))
    b.append(int(input("enter5")))
    a.append(b)
    j=0
    column=0
    row=0
    daigonal=0
    l=len(a)
    while j<l:
        row=row+a[i][j]
        column=column+a[j][i]
        daigonal=daigonal+a[j][j]
        j+=1
    i+=1
print(column,"column")
print(row,"row")
print(daigonal,"daigonal")
print()
if row==column==daigonal:
    print("magic square of table 5")
else:
    print("not a magic square")
print(a)

