odd_elements = lambda lst: list(filter(lambda x: x % 2 != 0, lst))

numbers = [1, 2, 3, 4, 5, 6, 7]
output = odd_elements(numbers)
print(output)
