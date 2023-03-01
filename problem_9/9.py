"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""


special_triplet = False

for a in range(1, 998):
    if special_triplet:
        break
    for b in range(a+1, 998):
        c = 1000 - a - b
        if c**2 == a**2 + b**2:
            print(a*b*c)
            special_triplet = True
            break



