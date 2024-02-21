def mint(lst, ending):
    try:
        filtered_list = list(filter(lambda x: x.endswith(ending), lst))
        return filtered_list
    except TypeError as e:
        print(f"Error: {e}")


words = ['hello', 'world', 'coding', 'nod']
ending = 'ing'
output = mint(words, ending)
print(output)
