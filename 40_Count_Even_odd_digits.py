#  Write a program to count the number of even digits and odd digits in a number n.

n = int(input("Enter the value of n: "))
even_count = 0 
odd_count = 0

while n != 0 :
    digit = n % 10
    
    if digit % 2 == 0:
        even_count += 1
    else: 
        odd_count += 1

    n = n // 10

print(f"Total Even digits = {even_count}")
print(f"Total Odd digits = {odd_count}")