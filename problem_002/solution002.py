# Solution to Project Euler Problem 2

def even_fibonacci_sum(limit):
    a, b = 1, 2  # First two Fibonacci numbers
    sum = 0

    while a <= limit:
        if a % 2 == 0:  # Check if the number is even
            sum += a
        a, b = b, a + b  # Move to the next Fibonacci numbers. Python evaluates the right-hand side first before making any assignments.

    return sum

result = even_fibonacci_sum(4000000)
print("The sum of even Fibonacci numbers below 4 million is:", result)
