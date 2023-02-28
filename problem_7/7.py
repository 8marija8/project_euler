"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""




x = 1

prime_numbers = []
not_prime = []

while len(prime_numbers) != 10001:
    x += 1
    for j in range(2, x+1):

      
      
      if x % j == 0 and x == j and x not in not_prime:
           prime_numbers.append(x)

      elif x % j == 0 and x != j: 
          not_prime.append(x)
          break
          
         
      


print("prime", prime_numbers)
print(prime_numbers[10_000])













