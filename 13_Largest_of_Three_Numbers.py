# Write a program to read three numbers and find the largest among them.

a = int(input("Enter the first Number : "))
b = int(input("Enter the second Number : "))
c = int(input("Enter the third  Number : "))

if(a >= b and a >= c):
    print(f"{a} is Largest Number. ")

elif(b >= a and b >= c):
    print(f"{b} is Largest Number. ")
    
else:
    print(f"{c} is Largest Number. ")
    
