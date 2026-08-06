# Write a program to swap two numbers using a third variable.

a  = int(input("Enter the first number : "))
b  = int(input("Enter the Second number : "))


print("\nBefore Swaping")
print(f"FIRST NUMBER = {a}")
print(f"SECOND NUMBER = {b}")

# Swapping using a third variable. 
c = a
a = b
b = c

print("\nAfter Swaping")
print(f"FIRST NUMBER ={a} ")
print(f"SECOND NUMBER ={b} ")