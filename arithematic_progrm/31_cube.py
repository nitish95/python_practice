# Write a Python Program for cube sum of first n natural numbers?

def cube_of_natural_no(n):
    if n<0:
        return 0
    else:
        total = sum([i**3 for i in range(1, n + 1)])
        #total = sum([i**3 for i  in range(1,n+1)])
        return total
    

n = int(input("Enter the natual number: "))

if n <=0:
    print("Enter a valid number.")
else:
    result = cube_of_natural_no(n)
    print(f"Cube of first {n} natural number is: {result}")