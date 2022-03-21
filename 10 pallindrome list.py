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




# num=input("item u want to store\n")
# item=list(num)
# list1=[]
# i=-1
# while i>=(-len(item)):
#     list1.append(num[i])
#     i-=1
# if list1==item:
#     print("it's a palindrome list")
# else:
#     print("not a palindrome list ")
# print("the list is",item)



# i=0
# a=[]
# while i<5:
#     user=int(input("enter:"))
#     a.append(user)
#     i+=1
# j=0
# l=0
# while j<len(a):
#     if a[j]>l:
#         l=a[j]
#     j+=1
# k=0
# s=a[k]
# while k<len(a):
#     if a[k]<s:
#         s=a[k]
#     k+=1
# print(l,s)




# h=[4,2,7,10,5,9,7,20,6]
# i=0
# a=[]
# while i<len(h):
#     j=0
#     c=0
#     while j <len(h):
#         if h[j]>h[i]:
#             c+=1
#         j+=1
#     a.append(c)
        
#     i+=1
# print(a)


# string=input("enter sentence")
# string="A man, a plan, a canal:Panama"
# a=""
# b=""
# i=0
# while i<len(string):
#     if string[i].isalnum():
#         a+=string[i]
#     i+=1
# x=a.lower()
# j=-1
# while j>=-len(x):
#     b+=x[j]
#     j-=1
# print('\"'+x+'\"')
# if x==b:
#     print('It\'s a palindrome sentence')
# else:
#     print(False)





num=[1,2,3,4]
i=0
a=[]
c=0
while i <len(num):
    x=num[i]+c
    c=x
    a.append(c)
    i+=1
print(a)