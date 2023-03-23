""" 


The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


"""


truncatable_primes = []
primes = []

for i in range(2, 1_000_000):
    is_prime = True

    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(i)



def is_truncable(number_left, number_right):
    
    while True:
        
        
        if len(str(number_left)) == 1:
            if number_left in primes:
                
                if len(str(number_right)) == 1:
                    if number_right in primes:
                        return True
             
                else:
                    number_right = int(str(number_right)[1::])
                    if number_right not in primes:
                        return False
                  
                
        
        else:
            number_left = int(str(number_left)[:-1:])
            if number_left not in primes:
                return False
            

num = 4

while len(truncatable_primes) < 11:
    
    if is_truncable(primes[num], primes[num]):
        truncatable_primes.append(primes[num])
    
    num += 1

print(truncatable_primes)
print(sum(truncatable_primes))