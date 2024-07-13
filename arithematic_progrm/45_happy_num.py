#Write a Python program to check if the given number is Happy Number.

def is_happy_num(num):
    seen = set()

    while num !=1 and num not in seen:
        seen.add(num)
       # print(f"{num} seen add number.")
        num = sum (int(i) ** 2 for i in str(num))
        print(f"{num} itterate num. ")
    
    return num == 1

num = int(input("Enter the number: "))

if is_happy_num(num):
    print(f"{num} is a happy number" )
else:
    print(f"{num} is not a happy number.")