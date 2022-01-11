list=[]
user=int(input("enter:"))
i=0
even=0
odd=0
ev=[]
od=[]
while i<=user:
    n=int(input("enter the number:"))
    list.append(n)
    if list[i]%2==0:
        even+=1
        ev.append(list[i])
    else:
        odd+=1
        od.append(list[i])

    i+=1
print("numbers of even number =",even,"\n they are: ",ev)
print("numbers of odd numbers =",odd,"\n they are: ",od)


