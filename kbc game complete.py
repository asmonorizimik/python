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

fifty_life=[["Eight","Seven"],["Bhopal","Delhi"],["Software-engineering","Tourism"]]
fiftyans=[2,2,1]
i=0
a=0
while i<len(q):
    print(i+1,q[i])
    j=0
    while j<=len(opt):
        print("  "+str(j+1)+":",opt[i][j])
        j+=1
    answer=int(input("enter your ans: "))
    if answer==ans[i]:
        print("CONGRATS")
    elif answer==5050:
        if a==0:
            b=0
            while b<len(fifty_life[i]):
                print("  "+str(b+1)+":",fifty_life[i][b])
                b+=1
            a+=1
            ans5050=int(input("enter your answer 5050: "))
            if ans5050==fiftyans[a]:
                print("correct answer ")
            else:
                print("wrong answer ")
                break
        else:
            print("you already used 5050 lifeline\n")
            n=int(input("enter:"))
            if n==ans[i]:
                print("CONGRATS you won the game with 5050")
            else:
                print("wrong")
                break

    else:
        print("wrong answer\ngame over")
        break
    i+=1
