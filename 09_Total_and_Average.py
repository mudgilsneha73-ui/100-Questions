# Write a program to read the marks of 5 subjects and print the total and average.

marks1 = int(input("Enter your English marks : "))
marks2 = int(input("Enter your Maths marks : "))
marks3 = int(input("Enter your Hindi marks : "))
marks4 = int(input("Enter your Science marks : "))
marks5 = int(input("Enter your Social Science marks : "))

total_marks = marks1 + marks2 + marks3 + marks4 + marks5
average = total_marks / 5

print(f"Your Total Marks = {total_marks} / 500")
print(f"Average Marks = {average}")