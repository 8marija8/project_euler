"""

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

"""

x = 0

for p_200 in range(0, 201, 200):
    for p_100 in range(0, 201, 100):
        for p_50 in range(0, 201, 50):
          for p_20 in range(0, 201, 20):
             for p_10 in range(0, 201, 10):
              for p_5 in range(0, 201, 5):
                for p_2 in range(0, 201, 2):
                  for p_1 in range(0, 201, 1):
                     total = p_1 + p_2 + p_5 + p_10 + p_20 + p_50 + p_100 + p_200
                     if total > 200:
                        break
                     if total == 200:
                        x += 1
                        
print(x)      