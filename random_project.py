import random
Cnumber=random.randrange(1,101)
userInput=int(input("enter your number:--"))
if userInput>Cnumber:
    print("Computer Number", Cnumber)
    print("Your guess number is high")
elif Cnumber>userInput:
    print("Computer Number", Cnumber)
    print("Your guess number is low")
else:
    print("Computer Number", Cnumber)
    print("your guess number is equal")