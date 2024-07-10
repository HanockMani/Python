def print_number_pyramid(height):
    for i in range(1, height + 1):
        for j in range(height - i):
            print(" ", end="")
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

def main():
    try:
        height = int(input("Enter the height of the pyramid: "))
        if height <= 0:
            print("Please enter a positive integer.")
        else:
            print_number_pyramid(height)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


main()

