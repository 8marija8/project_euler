import math


number = 600851475143
prime_factors = []

for x in range(2, math.floor((math.sqrt(number + 1)))):
    if number % x == 0:
        prime_factors.append(x)
        number /= x

print(max(prime_factors))
print("prime factors: ", prime_factors)








