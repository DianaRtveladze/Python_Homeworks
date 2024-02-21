"""
Arithmetical Operations using two parameters: 
1. Sum of two numbers
2. Subtraction
3. Multiplication
4. Division
5. Power
"""

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

sum = first_number + second_number
subt = first_number - second_number
mult = first_number * second_number
if second_number != 0:
    div = first_number / second_number
power = first_number ** second_number

print("Sum:", sum,
      "\nSubtraction:", subt, 
      "\nMultiplication:", mult, 
      "\nDivision:", div, 
      "\nPower:", power)

 