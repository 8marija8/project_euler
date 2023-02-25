"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""







num = 20

while True:
  if all(num % i == 0 for i in range(1,21)):
    print(num)
    break
  num += 20




