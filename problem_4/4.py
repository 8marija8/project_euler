"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


"""


palindromes = []

for i in range(999,0,-1):
    for j in range(999,0,-1):
        
        product = str(i*j)
        reverse = product[::-1]

        if product == reverse:
            
            product = int(product)
            palindromes.append(product)


print(max(palindromes))



































