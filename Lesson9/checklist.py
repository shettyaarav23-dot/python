total_activity=int(input("how many activites are there"))
count=1
while True:
    if count>total_activity:
        break
    a=input("enter your activity")
    print(a)
    count=count+1
    
task=4
i=0
while i<task:
    n=int(input("enter a number between 1-4"))
    if n==1:
        print("cricket")
    elif n==2:
        print("football")
    elif n==3:
        print("tennis")
    elif n==4:
        print("badmintion")
    else:
        print("invalid number")

