# Write a Python Program to Check if a Number is Odd or Even

def check(n):
    if n%2 == 0:
        return "Even number"
    else:
        return "Odd number"

number= int(input("Enter the number: "))
print(check(number))