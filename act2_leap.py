# Name: Magahis Frank
# Section: BMET 2101
# Task 3: Leap Year Test

year = int(input("Enter a year: "))

is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap_year)