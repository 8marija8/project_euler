<<<<<<< HEAD
"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""




=======
>>>>>>> b4111ba430cb19aeea9450e7af34b151a07d8b9f
import math


number = 600851475143
prime_factors = []

for x in range(2, math.floor((math.sqrt(number + 1)))):
    if number % x == 0:
        prime_factors.append(x)
        number /= x

print(max(prime_factors))
print("prime factors: ", prime_factors)








