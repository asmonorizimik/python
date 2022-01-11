####[[11,19], [12,18],[13,17] output


number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
m=[]
while i<len(n):
    j=0
    a=[]
    while j<len(n):
        if n[i]+n[j]==number and n[j]<n[i]:
            a.append(n[i])
            a.append(n[j])
            m.append(a)
        j+=1
    i+=1
print(m)



