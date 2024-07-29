#Write a Python Program to Find Factorial of Number Using Recursion

# 𝑛! = 𝑛 × (𝑛 − 1) × (𝑛 − 2) × … × 3 × 2 × 1

def fact(n):
    if n==1:
        return 1
    else:
        return (n * fact(n-1))

num = int(input("Enter the limit: "))

print(f"Factorial of ", +num,"! is: ", fact(num))