
a = [16, 19, 11, 15, 10, 12, 14]
# a=[1,21,3,14,5]
j=0
while j<len(a):
    i = 0
    while i<len(a)-1:
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
        i = i+1
    j+=1
    # print (a)
# print()
print(a,"the sorted numbers")



# a=[12,0,39,50,1]
# i=0
# while i<len(a):
#     b=i
#     j=0
#     while j<len(a):
#         if a[b]>a[j]:
#             b=1
#         j+=1
#     a[i],a[b]=a[b],a[i]
#     i+=1
#     print(a)

