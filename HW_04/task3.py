import random

guessNumber = random.randint(1, 100)

while(True):
    number = int(input("Number? "))
    if(number == guessNumber):
        print("The correct number is ", guessNumber)
        break
    elif(number < guessNumber):
        print("Too low")
    else:
        print("Too high")