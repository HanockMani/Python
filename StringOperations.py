def check_substring(main_string, sub_string):
    return sub_string in main_string

def count_occurrences(string, char):
    return string.count(char)

def replace_substring(string, old_sub, new_sub):
    return string.replace(old_sub, new_sub)

def convert_to_capital(string):
    return string.upper()

def main():
    while True:
        print("\nString Operations Menu:")
        print("1. Check if the String is a Substring of Another String")
        print("2. Count Occurrences of Character")
        print("3. Replace a Substring with Another Substring")
        print("4. Convert to Capital Letters")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            main_string = input("Enter the main string: ")
            sub_string = input("Enter the substring to check: ")
            if check_substring(main_string, sub_string):
                print(f"'{sub_string}' is a substring of '{main_string}'")
            else:
                print(f"'{sub_string}' is NOT a substring of '{main_string}'")
                
        elif choice == '2':
            string = input("Enter the string: ")
            char = input("Enter the character to count: ")
            count = count_occurrences(string, char)
            print(f"The character '{char}' occurs {count} times in '{string}'")
        
        elif choice == '3':
            string = input("Enter the string: ")
            old_sub = input("Enter the substring to replace: ")
            new_sub = input("Enter the new substring: ")
            new_string = replace_substring(string, old_sub, new_sub)
            print(f"The new string is: '{new_string}'")
        
        elif choice == '4':
            string = input("Enter the string: ")
            capital_string = convert_to_capital(string)
            print(f"The string in capital letters is: '{capital_string}'")
        
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

main()