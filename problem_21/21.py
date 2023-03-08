"""

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""


amicable_numbers =  set()

def amicable(num):

  first_divisors = [i for i in range(1,num) if num % i == 0]

  sum_first_divisors = sum(first_divisors)

  second_divisors = [i for i in range(1,sum_first_divisors) if sum_first_divisors % i == 0]

  sum_second_divisors = sum(second_divisors)


  if num == sum_second_divisors and num != sum_first_divisors:
     amicable_numbers.add(num)
     amicable_numbers.add(sum_first_divisors)


num = 1


while num < 10_000:
  amicable(num)
  num += 1



print(sum(amicable_numbers))