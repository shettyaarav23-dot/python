print("welcome to the number guessing game")
print("in this game there is a number that you have to guess which is between 1-50")
print("you will have 5 chances to guess this number")
print("after every incorrect guess you will receive a hint")
print("good luck")
secret=34
lives=5
while lives>0:
    guess=int(input("guess the number"))

    if guess==secret:
        print("congratulations you win")
        break
    elif guess>secret:
        print("the number is less than this")
    elif guess<secret:
        print("the number is greater than this")
    
    else:
        print("thats wrong try again")
    lives=lives-1
    
    



if lives==0:
    print("you are out of lives try again")
    
