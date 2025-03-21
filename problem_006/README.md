# Problem 6 - Sum Square Difference

The sum of the squares of the first ten natural numbers is:

$$
1^2 + 2^2 + ... + 10^2 = 385$$

The square of the sum of the first ten natural numbers is:

$$
(1 + 2 + ... + 10)^2 = 55^2 = 3025
$$

The difference between the sum of the squares and the square of the sum for the first ten natural numbers is:

$$
3025 - 385 = 2640
$$

Find the difference between the sum of the squares and the square of the sum for the first 100 natural numbers.

# Approach

  The sum of the squares of the first n natural numbers can be calculated iteratively or using a formula:
  
  $$
  (1^2 + 2^2 + ... + n^2) = \frac{n \times (n+1) \times (2n+2)}{6}
  $$


  The square of the sum of the first n natural numbers can be calculated iteratively or using a formula:

  $$
  \Bigg( \frac{n(n+1)}{2} \Bigg) ^2
  $$
  
\[
\Bigg( \frac{n(n+1)}{2} \Bigg)^2
\]

  
# RunTime Analysis

O(1) with optimized formulas
