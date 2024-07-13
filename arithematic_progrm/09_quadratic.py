#Write a Python program to solve quadratic equation.

# 𝑎𝑥^2 + 𝑏𝑥 + 𝑐 = 0

import math

a=float(input("Enter value of a: "))
b=float(input("Enter value of b: "))
c=float(input("Enter value of c: "))

discriminant = (b*b-4*a*c)

# Check if the discriminant is positive, negative, or zero
if discriminant >0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root1 {root1}")
    print(f"Root2 {root2}")

elif discriminant ==0:
    root = (-b/ (2*a))
    print("Root {root}")

else:
    print("The equation has no real roots.")