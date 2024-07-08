#Write a Python program to convert Celsius to Fahrenheit.

# C = (F − 32) × 5 ⁄ 9

C= float(input("Enter the Temperature in Celcius: "))

F= (C*9/5) +32
print(f"Converted temperature: {F}")