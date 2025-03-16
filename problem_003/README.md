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

If a number larger than sqrt(n) were a factor, its corresponding co-factor would already be found below that value.

By the time we reach sqrt(n), any leftover number must be prime itself.

## RunTime
O(sqrt(N))
