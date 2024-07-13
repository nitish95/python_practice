#Write a Python program to swap two variables without temp variable.

a = (int(input("Enter the original value of a: ")))
b = (int(input("Enter the original value if b: ")))

a = a + b
b = a - b
a = a - b

print(f"Swapped value of a: {a}") 
print(f"Swapped value of b: {b}")