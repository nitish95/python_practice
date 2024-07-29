# Write a Python Program to Find the Factorial of a Number.

num = int(input("Enter a number: "))
Fatorial = 1

if num < 0:
    print("Factorial not possible.")
elif num == 0:
    print(f"Factorial of {num} is: 1")
else:
    for i in range(1, num+1):
        Fatorial = Fatorial*i
    print(f"Factorial of {num} is: {Fatorial}")