# Solution to Project Euler Problem 4

def is_palindrome(n):

    return str(n) == str(n)[::-1]

def largest_palindrome_product():
    max_palindrome = 0
    for i in range(999, 99, -1):      # Go downwards from 999 to 100
        if i * 999 < max_palindrome:  # Stop early if max possible product is too small
            break
        for j in range(i, 99, -1):  # Go downwards from i to 100, Only check j ≤ ix to avoid duplicates
            product = i * j
            if product <= max_palindrome:  # Break if product is smaller than known max
                break
            if is_palindrome(product):
                max_palindrome = product

    return max_palindrome

# Test
result = largest_palindrome_product()
print("The largest palindrome made from the product of two 3-digit numbers is:", result)
