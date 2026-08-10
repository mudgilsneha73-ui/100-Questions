#  Write a program to reverse a number n.

n = int(input("Enter the value of n: "))
reverse = 0
while n != 0:
    digits = n % 10
    reverse = reverse * 10 + digits
    n = n // 10

print("Reverse = ",reverse)
    