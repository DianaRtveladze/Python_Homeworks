import re

def validate_phone_number(phone_number):
    # regex expression
    pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{3}$')

    if pattern.match(phone_number):
        return phone_number
    else:
        return "Invalid format"

def main():

    user_input = input("Enter a phone number (e.g., (123) 456-789): ")
    result = validate_phone_number(user_input)
    print(result)

if __name__ == "__main__":
    main()
