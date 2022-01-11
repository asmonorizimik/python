
str = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
substr = "on "
a=str.split(" ")
n=" "
i=0
while i<len(a):
    if a[i]=="over":
        n=n+substr   
    else:
        n=n+a[i]+" "  
    i+=1
b=n.split()
print(b)