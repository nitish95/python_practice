# Write a Python Program to Display Fibonacci Sequence Using Recursion.

# recurrence relation ( F(n) = F(n-1) + F(n-2) )

def fibonacci(num):
    if num <2:
        return num
    else:
        return (fibonacci(num-1) + fibonacci(num-2))
    
nterm=int(input("Enter the fibonacci limit: "))

if nterm <=0:
    print("Print a valid integer.")
else:
    print("Fibonacci seq: ")
    for i in range(nterm):
        print(fibonacci(i))