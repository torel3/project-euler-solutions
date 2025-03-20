## Problem 5 - Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is **evenly divisible** by all of the numbers from 1 to 20?

## Approach

We use the Least Common Multiple (LCM) approach.

The LCM of two numbers `a` and `b` is:
  
  
  $$
  LCM(a, b) = \frac{a \times b}{GCD(a, b)}
  $$
  
  
We compute Greater Common Diviser (GCD) using the built in function math.gcd().

For the sake of clarity we provide the code of this function that uses Euclidean algorithm.

## RunTime

The Euclidean algorithm for GCD runs in O(log N) time (every step reduces one number by half on average).

LCM takes O(log N) per calculation.

We iterate over n numbers.

The total RunTime is O(N log N).
