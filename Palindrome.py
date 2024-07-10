def reverse_number(n):
    reversed_num = int(str(n)[::-1])
    return reversed_num

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def make_palindrome(n):
    steps = 0
    while not is_palindrome(n):
        reversed_num = reverse_number(n)
        n += reversed_num
        steps += 1
        print(f"Step {steps}: {n} (after adding {reversed_num})")
    return n

def main():
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Please enter a non-negative integer.")
        else:
            result = make_palindrome(number)
            print(f"The resulting palindrome is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

main()