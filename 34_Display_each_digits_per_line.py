#   Write a program to display all the digits of a number n (one per line)

n = int(input("Enter the value of b n: "))

digit = 0

while n != 0:
    digit = n % 10 

    print(digit) 
    
    n = n // 10
    
