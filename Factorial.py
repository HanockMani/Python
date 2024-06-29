factorial_cache = {}

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n in factorial_cache:
        return factorial_cache[n]
    elif n == 0 or n == 1:
        factorial_cache[n] = 1
    else:
        factorial_cache[n] = n * factorial(n - 1)
    
    return factorial_cache[n]

number = 5
print(f"Factorial of {number} is {factorial(number)}")
print(f"Cached factorials: {factorial_cache}")