# Solution to Project Euler Problem 6

import math

def sum_of_squares(n):
    res = 1
    for i in range(n, 1, -1):
        res += i*i
    return res

def square_of_sum(n):
    res = 1
    return (n*(n+1)/2)**2


# Compute for n = 100
n = 100
result = square_of_sum(n) - sum_of_squares(n)
print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is:", int(result))
