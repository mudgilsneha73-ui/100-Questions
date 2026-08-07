# Write a program to read a number and check whether it is divisible by both 3 and 5

n = int(input("Enter the Number: "))

if(n % 3 == 0 and n % 5 == 0):            
    print(f"{n} is Divisible by both 3 and 5")
else:
    print(f"{n} is not Divisibe by both 3 and 5")

# Another valid approach : check n % 15 == 0 because 15 is the LCM of 3 and 5.