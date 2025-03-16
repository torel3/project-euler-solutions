# Solution to Project Euler Problem 3

def largest_prime_factor(n):
    # Remove factors of 2 first
    while n % 2 == 0:
        n //= 2

    # Check odd numbers from 3 onwards up to square(n).
    # If a number larger than square(n) were a factor, its corresponding co-factor would already be found below that value.
    # By the time we reach square(n), any leftover number must be prime itself.

    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            n //= factor  # Divide n by factor
        factor += 2  # Move to the next odd number

    # If n is still greater than 2, it's a prime number itself
    return n if n > 2 else factor - 2

# Test for the given number
num = 600851475143
result = largest_prime_factor(num)
print("The largest prime factor of", num, "is:", result)
