
total_sum = 0

while(True):
    number = input("Add number: ")
    if(number.lower == "sum"):
        print("The sum of entered numbers is: ", total_sum)
        break
    elif(float(number) >= 0):
        total_sum += float(number)
    else:
        continue