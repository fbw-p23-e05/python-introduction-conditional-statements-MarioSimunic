num = float(input("Input the radius of the circle: "))

import math
res = round(float(math.pi*(num**2)), 2)
print("The area of the circle with radius ", num, " is: ", res)