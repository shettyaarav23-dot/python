is_raining=input("enter yes if it is raing or not")
wind_speed=int(input("what is the wind speed"))
temperature=int(input("enter the temperature"))
if temperature>30:
    print("it is hot outside")
    
else:
    print("it is not hot")
    

if is_raining== "yes":
    print("bring umbrella")
else:
    print("dont bring umbrella")

if wind_speed>35:
    print("it is a windy day")
else:
    print("it is a calm day")
print("the wind speed is", wind_speed)
print("the temperatue is", temperature)
print("yes is is raining", is_raining)