list1 = [4,5,6,7,8,9]
list2 = [4,6,8,1,2,9]
i=0
diff=[]
while i<len(list1):
    if list1[i] not in list2:
        diff.append(list1[i])
    i+=1
print(diff)


