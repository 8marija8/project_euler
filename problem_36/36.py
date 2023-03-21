"""

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

"""


total_palindromes = 0

for number in range(1, 1_000_000):
    if number == int(str(number)[::-1]):
        binary = bin(number).replace("0b", "")
  
        if binary == binary[::-1]:
            total_palindromes += number

print(total_palindromes)
