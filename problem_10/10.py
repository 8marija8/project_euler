"""

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""


total = 0
number = 2

def is_prime(number):
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
      


while number < 2_000_001:
    if is_prime(number):
        total += number
    number += 1

print(total)