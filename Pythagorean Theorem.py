length_a = int(input("What is the length of side a?  "))
length_b = int(input("what is the length of side b?  "))

length_c_squared = length_a**2 + length_b**2

import math

length_c = math.sqrt(length_c_squared)

print ("The length of side C of this right triangle is")
print (length_c)