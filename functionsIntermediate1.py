#Write a single function, randInt(), that takes up to 2 arguments. If no argument is provided, return a random integer between 0 and 100, if only a max, 0 to max, if only a min, min to 100, and between the two if both are provided. Account for edge cases, such as min>max

import random
def randInt(min=0, max=100):
    if min < max:
      num = int(min+random.random()*(max-min))
      return num
    else:
      return False
print(randInt())	                    # should print a random integer between 0 to 100
print(randInt(max=50)) 	              # should print a random integer between 0 to 50
print(randInt(min=50)) 	              # should print a random integer between 50 to 100
print(randInt(min=50, max=500))       # should print a random integer between 50 and 500
print(randInt(min=500, max=50))       # should print false