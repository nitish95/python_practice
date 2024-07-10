#Write a Python Program to Display the multiplication Table

num = int(input("Enter a number: "))
m=1
for i in range(1, num+1):
    m=i*num
    print(f"{num} x {i} = {m}")