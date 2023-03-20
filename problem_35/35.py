"""


The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?


"""

primes = []
for i in range(2, 1_000_000):
    is_prime = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
      primes.append(i)

circular_primes = []

total = 0
for number in primes:
    if len(str(number)) == 1:
        total += 1
        circular_primes.append(number)
        continue
    
    num = number
    for combination in range(1,len(str(num))):    
        
        if len(str(num)) == len(str(number)):
          rotation = int(str(number)[1:] + str(number)[0])
        else:
            rotation = int(str(number)[1:] + str(number)[0] + str(0))

        if rotation in primes:
            number = rotation
            if combination == len(str(num)) - 1:
                total += 1
                circular_primes.append(num)
            
        else:
            break
    

print("total: ", total)