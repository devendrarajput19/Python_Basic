# 1 - To check leap year using if else

# year = int(input("Enter any year: "))

# if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a Leap year")
# else:
#     print(year, "is not a Leap year")

# 2 - Using function

# def leapyear(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# year = int(input("Enter any year: "))

# if(leapyear(year)):
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")

# 3 - using Calender module

import calendar

year = int(input("Enter any year: "))

if(calendar.isleap(year)):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap year")