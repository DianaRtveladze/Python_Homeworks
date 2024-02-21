num_list = [44, 23, 11, 8, 20, 56, 33, 55]

num = int(input("Enter the number: "))

if (num > num_list[2]) and (num < num_list[-1]):
    print("More than list elements")
elif(num == num_list[5]):
    print("Equal")
else:
    print("None of the conditions were met")