
# numbers = [1,2,5,8,4,9,3]
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i = 0
lar=0
while i < len(numbers):
  if numbers[i] > lar:
    lar = numbers[i]
  i = i+1
print (lar,"is the largest element")
                       

