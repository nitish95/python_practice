#Write a Python Program to Check Leap Year.

# divided by 100 means century year (ending with 00)
# year divided by 4 is a leap year


def leap_year(yr):
    if yr % 4==0 and yr % 400 == 0 and yr % 100 == 0:
        return "Leap Year!!!"
    elif yr % 4 == 0 and yr % 100 != 0 and yr % 400 != 0:
        return "Leap Year!!!"
    else:
        return "No Leap year"
    
year= (int(input("Enter the year: ")))
print(leap_year(year))