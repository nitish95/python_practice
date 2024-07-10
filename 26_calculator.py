#Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations.

def add(x,y):
    return x+y

def subs(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y

print("Addition: ")
print("Substract: ")
print("Multiply: ")
print("Division: ")

while True:
    choice = input("Enter the 1/2/3/4: ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1= float(input("Enter first value: "))
            num2= float(input("Enter second value: "))
        except ValueError:
            print("Invalid input.xxxxxx")
            continue

    if choice == '1':
        print(num1, '+', num2,'=',add(num1,num2))
    elif choice == '2':
        print(num1, '-', num2,'=',subs(num1,num2))
    elif choice == '3':
        print(num1, '*', num2,'=',mult(num1,num2))
    elif choice == '4':
        print(num1, '/', num2,'=',div(num1,num2))

    next_calculation = input("Lets do the next calculation: (yes/no)?")
    if next_calculation == 'no':
        break
    else:
        print("invalid input")