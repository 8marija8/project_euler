"""

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

"""

not_found = True
number = 1

while not_found:
    
  number += 1
  x_2 = number * 2
  x_3 =  number * 3
  x_4 = number * 4
  x_5 = number * 5
  x_6 = number * 6

  for digit in str(number):
    same_digits = True

    if digit not in str(x_2) or digit not in str(x_3) or digit not in str(x_4) or digit not in str(x_5) or digit not in str(x_6) or len(str(number)) != len(str(x_2)) or len(str(number)) != len(str(x_3)) or len(str(number)) != len(str(x_4)) or len(str(number)) != len(str(x_5)) or len(str(number)) != len(str(x_6)):

      same_digits = False
      break
  
  if same_digits:
    print(number)
    break
    
    
