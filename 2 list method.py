
#### 1.method to change list
# thelist=["apple","banana","mango","grapes","kiwi"]
# thelist[4]="pineapple"
# print(thelist)
# # change the list by indexing ...indexing means taking out single item from the list



# ## 2.method to insert new item without replacing any existing item:insert()
# thelist=["apple","banana","mango","grapes","kiwi"]
# thelist.insert(3,"watermelon")
# print(thelist)
## watermelon instead of grapes, grapes located at index 3
##it shows the index and the item we want to put inside the list


# 3.list=[1,2,3,4,6,7,9,]
# list.insert(0,0) or list.insert(5,5) or list.insert(8,8)
# print(list)
# print(type(list[1]))



####4.method to add list at the end of the list:append()

# list=[1,2,3,4,5]
# list.append(6) or list.append(7)
# print(list) 

###5. method to extend element from another list to the current list: extend()
# list1=[0,1,2,3,4,5,]
# list2=[6,7,8,9]
# list1.extend(list2) or list1.extend("p")
# print(list1)


###6.method to remove specified item: remove()
# list=[0,1,2,3,7,4,5,6,8,7,8,9]
# list.remove(7)  or list.remove(8) ##should take arguement if no argument, its error
# print(list)




##7.method to remove specified index:pop() without index, it removes the last item
# list=[0,1,2,3,4,5,5,6,7]
# list.pop(5)
# print(list)


###8.del keyword to remove the item
# list=[0,0,1,2,3,4,5]
# del list[:5] # can remove in range or index also
# print(list)


##9.method to clear all the method
# list=[0,1,2,3,4,5,6]
# list.clear()
# print(list)   ##cannot take an arguement


###10.join one list to another list

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.append(list2)
# print(list1)
# for x in list2:
#   list1.append(x)
# print(list1) 

##11.extend list after another list
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1) 


# ###12.sort method will sort the list alphanumerically, ascending by default
# list=[1,5,6,3,9,2,10,45,7,32]
# list.sort()
# # list.sort(reverse=True)
# print(list)


# list=[9,4,23,6,4,87,54,65]
# list.insert(0,"manori")
# print(list)
# list.reverse()
# print(list)


##case sensitive sorting
# list=["A","P","g","a","h","l"]
# list.sort()
# print(list)


##13.copy method
# list=[1,5,6,3,9,2,10,45,7,32]
# list1=list.copy()
# list1.sort()
# print(list1)


###14.joining method
# list=[1,5,6,3,9,2,10,45,7,32]
# list.sort()
# list1 = ["a", "b" , "c"]
# list2=list+list1
# print(list2)


###15 count method...used  when there are duplicate items
# item=["a","b","a","c"]
# c=item.count("a")
# print("count of a:",c)



##16 method to split the string value and execute to list 
# str="we learn software skills in ng"
# a=str.split()
# print(a)


