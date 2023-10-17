import math
print("This program calculates the length of the hypotenuse of a right triangle.")
print("Please enter the lengths of sides A and B.")
A = float(input("Length of side A: "))
B = float(input("Length of side B: "))
C = math.sqrt(A**2 + B**2)
print("The length of the hypotenuse (side C) is:", C)