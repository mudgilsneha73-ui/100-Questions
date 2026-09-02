# Write a program to check whether a number is a Harshad (Niven) number

n = int(input("Enter the value of n: "))

original = n
digit_sum = 0

while n != 0:
    digit = n % 10
    n = n // 10
    digit_sum += digit

if original % digit_sum  == 0:
    print("Harshad Number")
else:
    print("Not Harshad Number")