# Solution to Project Euler Problem 5

import math

def lcm(a, b):
    # The Least Common Multiple of a and b
    # There is a built in function: math.gcd(), but it will be provided below for the purpose of clarity
    return abs(a * b) // math.gcd(a, b)

def smallest_multiple(n):
    #  The smallest number that is evenly divisible by all numbers from 1 to n
    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    return result

# Here is the gcd function that computes the Greatest Common Divisor (GCD) using the Euclidean algorithm.
def gcd(a, b):
    while b:
        a, b = b, a % b  # Keep dividing until b becomes 0
    return a

# Compute for numbers from 1 to 20
result = smallest_multiple(20)
print("The smallest multiple evenly divisible by all numbers from 1 to 20 is:", result)
