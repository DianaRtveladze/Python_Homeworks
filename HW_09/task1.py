def group_lists(list1, list2):
    grouped_list = list(zip(list1, list2))
    return grouped_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
output = group_lists(list1, list2)
print(output)
