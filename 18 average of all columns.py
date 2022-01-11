marks = [[78, 76, 94, 86, 88],
[91, 71, 98, 65, 76],
[95, 45, 78, 52, 49]]
i=0
while i<len(marks):
    j=0
    sum=0
    l=len(marks[i])
    while j<l:
        sum=sum+marks[i][j]
        j+=1
    i+=1
    average=sum/l
    print(j,"= number of marks in year")
    print(sum,"= total marks of year",i)
    print(average,"= average of year",i)
    print()


