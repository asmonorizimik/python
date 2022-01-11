marks = [
[78, 76, 94, 86, 88],
[91, 71, 98, 65, 76],
[95, 45, 78, 52, 49]
]
i=0
sum=0
while i<len(marks):
    j=0
    count=0
    while j<len(marks[i]):
        count+=1
        sum=sum+marks[i][j]
        j+=1
    i+=1
    totalcount=count*i
    average=sum/totalcount
print(count,"number of items in each list")
print(totalcount,"number of all items in list")
print(sum,"total sum")
print(average,"average")
   




