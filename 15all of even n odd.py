list=[]
user=int(input("enter how many numbers you want:"))
i=0
even=0
odd=0
ev=[]
od=[]
sumofeven=i
sumofodd=i
total_sum=i
allaverage=0
av_of_even=0
av_of_odd=0
while i<user:
    n=int(input("enter the list:"))
    list.append(n)
    total_sum=list[i]+total_sum
    allaverage=total_sum/user
    if list[i]%2==0:
        sumofeven=list[i]+sumofeven
        even+=1
        av_of_even=sumofeven/even
        ev.append(list[i])
    else:
        sumofodd=list[i]+sumofodd
        odd+=1
        av_of_odd=sumofodd/odd
        od.append(list[i])

    i+=1
print("the list is:",list)
print("numbers of even number in the list =",even,"\n they are: ",ev)
print("sum of even =",sumofeven)
print("average of all even numbers =",av_of_even)

print("numbers of odd numbers in the list =",odd,"\n they are: ",od)
print("sum of odd =",sumofodd)
print("average of all odd numbers =",av_of_odd)

print("sum of all items in the list =", total_sum)
print("average of all the items in the list =",allaverage)
print("total number of all items in the list =",i)
