# Write a program to read a year and check whether it is a leap year or not.

year = int(input("Enter the Year : "))

if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print(f"{year} is a Leap Year. ")
else:
    print(f"{year} is not a Leap Year!")
