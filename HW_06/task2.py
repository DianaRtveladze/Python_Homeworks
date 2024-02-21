
# Index of 210
my_list = [43, '22', 12, 66, 210, ["hi"]]
index_210 = my_list.index(210)
print(f"Index of 210: {index_210}")

# Add the text "hello" to the last element
last_element = my_list[-1]
if isinstance(last_element, list):
    last_element.append("hello")
else:
    my_list[-1] = [last_element, "hello"]

# Delete the element at the second index and print the list
del my_list[2]
print("List after deleting element at index 2:", my_list)

# Create a new list my_list_2, clear my_list_2, and print both lists
my_list_2 = my_list.copy()
my_list_2.clear()

print("Original list:", my_list)
print("New list (my_list_2) after clearing:", my_list_2)
