# How to make an algorithm
# 1: Define the Tast
# 2: Develop the algoritm
# 3: Write down the algoritm
# 4: Write the code
# 5: Test the code
# 6: Improve the code 
# 7: Document the code, write a manual

# Example of calculating pi in step 3 "plan english":
#   Algorithm: in ‘plain’ english
#1. Import necessary modules
#2. draw two uniform random numbers x, y between 0 and 1
#3. Calculate a distance d between the coordinate (0,0) and (x,y)
#4. Check whether d is smaller than r
#5. If d is smaller or the same as r add 1 to counter for the circle
#6. If d is larger then do nothing
#7. add 1 to the counter for the square
#8. go back to 2. until the square counter is larger than n
#9. print out the ratio of the circle/square * 4

import random
import math

# initialize variables
i = 0
n = 1000000
r = 1.0
circle = 0.0
square = 0.0

# Do many times
while i < n:
    i = i + 1
    # Draw x, y coordinate
    x = random.uniform(0.0, r)
    y = random.uniform(0.0, r)
    #calc d from center
    d = math.sqrt(x**2 + y**2)
    if d < r:
        circle = circle + 1
    square = square + 1
    
print(f"pi = {circle/square * 4.0}") 