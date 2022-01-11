q =[
"How many continents are there?",
"What is the capital of India?",
"what course do we learn in NG?"
]

opt= [
["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal","Chennai","Delhi"],
["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
ans = [3,4,1]
i=0
while i<len(q):
    print(i+1,q[i])
    j=0
    while j<=len(opt):
        print(j+1,opt[i][j])
        j+=1
    answer=int(input("enter your ans: "))
    if answer==ans[i]:
        print("CONGRATS")
    else:
        print("wrong answer\ngame over")
        break
    i+=1
    


    

