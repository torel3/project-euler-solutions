## Problem 4 - Largest Palindrome Product

A palindromic number reads the same both ways. 

The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

## Approach

Iterate through possible products.

Start with the largest 3-digit numbers (999 × 999) and iterate downwards.

Check if the product is a palindrome.

Keep track of the largest palindrome found.

Break when the product is smaller than the largest palindrome found.

## RunTime

O(n²)
