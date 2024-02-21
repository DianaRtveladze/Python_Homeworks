from functools import reduce

def calculate_product(numbers):
    try:
        product = reduce(lambda x, y: x * y, numbers)
        return product
    except TypeError:
        raise TypeError("Input must be a list of numbers")

# Example usage:
numbers = [1, 2, 3, 4, 5]
output = calculate_product(numbers)
print(output)
