###PALLINDROME
# list=["n","i","t","i","n"]
# list1=list.copy()
# list1.reverse()
# if list==list1:
#     print("palindrome list")
#     print(list)
# else:
#     print("not pallindrome list")


# print("How many element to store in the list: ", end="")
# n = int(input())
# mylist = []
# for i in range(n):
#     val = input("list item: ")
#     mylist.append(val)
#     list=mylist.copy()
#     list.reverse()
# if list==mylist:
#     print("pallindrome list")
# else:
#     print("not pallindrome")
# print("\nThe list is:",mylist)




num=input("item u want to store\n")
item=list(num)
list1=[]
i=-1
while i>=(-len(item)):
    list1.append(num[i])
    i-=1
if list1==item:
    print("it's a palindrome list")
else:
    print("not a palindrome list ")
print("the list is",item)






    


