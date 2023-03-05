"""

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

              [image: 2×2 grid]

How many such routes are there through a 20×20 grid?

"""





import math as m 


len_route = 40  # grid 20x20 --> 20 down + 20 right = 40 




def find_routes(length, *args):
  
  factorial_product = 1
  for i in args:
    factorial_product *= m.factorial(i) 
  routes = m.factorial(length) // factorial_product
  return routes



grid_20x20 = find_routes(len_route, 20,20)
print("number of routes: ", grid_20x20)



