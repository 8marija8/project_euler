"""

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

"""

from math import factorial

sum_equal_numbers = 0

for number in range(3, 10_000_000):
    digits = 0

    for digit in str(number):
        digits += factorial(int(digit))

    if digits == number:
        sum_equal_numbers += number

print(sum_equal_numbers)