## Problem 3 - Largest Prime Factor

The prime factors of 13195 are 5, 7, 13, and 29.

What is the largest prime factor of the number 600851475143?

## Approach

Remove factors of 2.

Divide the number by 2 repeatedly until it is odd.

Iterate through odd numbers.

Check divisibility starting from 3 up to sqrt(N).

If divisible, divide N completely by the factor.

Continue with the next odd number.

If N > 2 at the end, it is a prime factor.

The remaining N after division is the largest prime factor.

## RunTime
O(sqrt(N))
