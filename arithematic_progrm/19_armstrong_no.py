#Write a Python Program to Check Armstrong Number
# If we calculate 1^3 + 5^3 + 3^3 , we get , which is equal to 153

num = int(input("Enter a number: "))

num_str = str(num)
num_len = len(num_str)

sum_of_powers = 0
temp_num = num

while temp_num > 0:
    digit = temp_num %10
    sum_of_powers += digit ** num_len
    temp_num //= 10

if sum_of_powers == num:
    print(f"it is an armstrong number. {sum_of_powers}")
else:
    print(f"it is not an armstrong number {sum_of_powers}")
