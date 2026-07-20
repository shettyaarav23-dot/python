print("welcome to ride builder")
print("step one pick your vehicle")
print("one for bike and two for car")
choice=int(input("enter 1 or 2"))
if choice==1:
    print("you have chosen bike")
    print("pick your bike type scooter or mountain bike")
    bike_type=int(input("enter 1 for scooter and 2 for mountain bike"))
    if bike_type == 1:
        print("you have chosen scooter")
    elif bike_type == 2:
        print("you have chosen mountain bike")
    else: 
        print("enter a valid choice")
elif choice == 2:
    print("you have chosen car")
    print("pick your car type suv or nissan")
    car_type=int(input("enter 1 for suv and 2 for nissan"))
    if car_type == 1:
        print("you have chosen suv")
    elif car_type == 2:
        print("you have chosen nissan")
    else: 
        print("enter a valid choice")
else:
    print("enter valid choice")
    
