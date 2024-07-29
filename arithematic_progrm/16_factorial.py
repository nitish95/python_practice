# Write a Python Program to Find the Factorial of a Number.
def fact(n,val):
    if n<0:
        return "Invalid number."
    elif n == 0:
        return 1
    else:
        for i in range(1,n+1):
            val = val*i
        return val
#v=1
factorial=1
num= (int(input("enter the number: ")))        
print("Factorial of a number: ",+fact(num,factorial))
