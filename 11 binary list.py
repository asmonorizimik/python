b = [1,0,0,1,1,0,1,1]
i = -1
power=0
sum=0
while i>=(-(len(b))):   ##we take minus sign bcoz binary number solving should start from reverse
    n=b[i]*2**power
    sum=sum+n
    power+=1
    i=i-1
print(sum)
 

