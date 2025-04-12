# Problem 7 - 10 001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

Find the 10,001st prime number.

## Approach

A number `n` is prime if it is not divisible by any integer from 2 to √n.  
This optimization avoids unnecessary checks and improves performance.

Strategy:

- Start from 2 and check each number.
- Use the trial division method to test for primality.
- Keep a counter to count how many prime numbers have been found.
- Stop once the 10,001st prime is found.

## RunTime Analysis

Time Complexity: ~O(n√p), where `n` is the number of primes to find, and `p` is the size of candidate primes.
