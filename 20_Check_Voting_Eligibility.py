# Write a program to read the age of a person and check whether they are eligible to vote

age = int(input("Enter your Age: "))
if age < 0:
    print("Invalid age!")
elif(age >=18):
    print("You are Eligible to Vote.")
else:
    print("You are not Eligibl to Vote.")