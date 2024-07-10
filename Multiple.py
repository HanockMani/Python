def find_and_sum_divisibles():
    numbers = []
    total_sum = 0

    for i in range(101, 200):
        if i % 7 == 0:
            numbers.append(i)
            total_sum += i

    return numbers, total_sum

def main():
    numbers, total_sum = find_and_sum_divisibles()
    print("Numbers greater than 100 and less than 200 that are divisible by 7:")
    print(numbers)
    print(f"Sum of these numbers: {total_sum}")

main()