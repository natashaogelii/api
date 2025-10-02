def getDetails(name = "Princess",state = "Guest"):
    print(f"Name is {name} and State is {state}")

getDetails()  #no parameter
getDetails("Natasha") #single argument, assumed to be for the first parameter
getDetails("member") #single keyword argument
getDetails(name = "Ogeli", state = "Member") #2 keyword arguments