# Convert meters into centimeters, decimeters, millimeters, miles

meters = float(input("Enter meters: "))

miles = meters / 1609.34
decimeters = meters * 10
centimeters = meters * 100
millimeters = meters * 1000

print("Miles:", miles,
      "\nDecimeters:", decimeters, 
      "\nCentimeters:", centimeters, 
      "\nMillimeters:", millimeters)