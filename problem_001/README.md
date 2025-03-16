## Problem 1 - Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

## Approach

Iterate through numbers from 1 to 999.

Check if a number is divisible by 3 or 5 (n % 3 == 0 or n % 5 == 0).

If yes, add it to the sum.

## RunTime

O(n)
