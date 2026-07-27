print("atm cash dispenser")
while True:
    name=input("what is your name")
    amount=int(input("how much are you withdrawing"))
    print("the user name is" ,name)
    print("the amount is" ,amount)
    notes_500=amount//500
    amount=amount%500
    notes_100=amount//100
    amount=amount%100
    notes_50=amount//50
    remendier=amount%50
    print(f"to withdraw all these amount it reqeuires {notes_500} 500 rupees")
    print(f"{notes_100} 100 rupees")
    print(f"{notes_50} 50 rupees")
    print(f"{remendier} are the remendier")
    