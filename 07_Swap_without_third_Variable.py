# 7. Write a program to swap two numbers without using a third variable.

a  = int(input("Enter the first number : "))
b  = int(input("Enter the Second number : "))


print("\nBefore Swaping")
print(f"FIRST NUMBER = {a}")
print(f"SECOND NUMBER = {b}")

# Swapping using a third variable. 
a = a + b
b = a - b
a = a - b 

print("\nAfter Swaping")
print(f"FIRST NUMBER = {a} ")
print(f"SECOND NUMBER = {b} ")
