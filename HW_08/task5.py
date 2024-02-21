

def reverse_string_recursive(input_str):
    if len(input_str) == 0:
        return input_str
    else:
        return input_str[-1] + reverse_string_recursive(input_str[:-1])

result = reverse_string_recursive("Hello")
print(result)