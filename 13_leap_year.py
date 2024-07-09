#Write a Python Program to Check Leap Year.

# divided by 100 means century year (ending with 00)
# year divided by 4 is a leap year


year= int(input("Enter the year: "))

if (year%400 == 0) & (year%100 ==0):
    print("It is leap year!!!")
elif (year % 4 == 0) & (year % 100 != 0):
    print("It is a leap year")
else:
    print("No leap year!!!")