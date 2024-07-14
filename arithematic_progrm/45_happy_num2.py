def is_happy_num(num):
    rem = sum =0

    while (num > 0):
        rem = num%10
        sum = sum + (rem **2)
        num = num //10
    return sum

num = int(input("enter the number: "))
result = num

while (result !=1):
    result = is_happy_num(result)

if result == 1:
    print("happy number")
else:
    print("Not happy")
