def manage_list(command, number, num_list):
    if command == 'a':
        num_list.append(number)
    elif command == 'r':
        if number in num_list:
            num_list.remove(number)
        else:
            print(f"{number} not found in the list.")
    elif command == 'e':
        print("Exiting program.")
        return True
    else:
        print("Invalid command. Please use 'a', 'r', or 'e'.")
    return False

def main():
    num_list = []
    
    while True:
        user_input = input("Enter command with space: ").split()
        
        if len(user_input) != 2:
            print("Invalid input. Please enter a valid command.")
            continue
        
        command, number = user_input
        number = int(number)
        
        exit_program = manage_list(command, number, num_list)
        
        if exit_program:
            break
        
        print("Current list:", num_list)

if __name__ == "__main__":
    main()
