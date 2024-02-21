number = int(input("Enter number 'n': "))

if number < 0:
    print("Wrong")
else:
    while(number > 0):
        print(number)
        number -=1