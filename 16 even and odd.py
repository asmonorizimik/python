# list=[12,13,14,2,3,4,5,6,7,8,9,19]
# i=0
# even=[]
# odd=[]
# while i<len(list):
#     if list[i]%2==0:
#         even.append(list[i])
#     else:
#         odd.append(list[i])

#     i+=1
# print(even,"even")
# print(odd,"odd")




elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=[]
odd=[]
sum=i
while i<len(elements):
    sum=elements[i]+sum
    if elements[i]%2==0:
        even.append(elements[i])
    else:
        odd.append(elements[i])
    i+=1
    average=sum/i       ##average =total by count i.e total items in the list
print("total elements =",i)
print(sum)
print(average)
