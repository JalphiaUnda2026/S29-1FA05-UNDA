
import math

print("--- Distance Calculator between Two Points ---")


x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# 2. Compute the distance using pow() and sqrt() from the math library
# Formula: d = sqrt( (x2 - x1)^2 + (y2 - y1)^2 )
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# 3. Display the result clearly
print(f"\nThe distance between the two points is: {distance}")



# Why is using a library more practical than writing all calculations from scratch?

# Using a library is more practical because it provides pre-written, highly optimized, 
#and error-free functions like math.sqrt() and math.pow(), saving time and effort. 
# Writing these algorithms from scratch requires advanced knowledge of numerical methods and increases the chances of introducing bugs. Libraries allow programmers to focus 
# on solving the actual problem rather than reinventing fundamental mathematical operations.