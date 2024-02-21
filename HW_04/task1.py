# This program takes number "n" and writes the sum of numbers before "n" (n is not included)

number = int(input("Enter number 'n': "))

i = 0
sum = 0
while (i < number):
    sum += i
    i+=1

print("The sum of numbers is: ", sum)