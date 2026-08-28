#  Write a program to find the length of a string without using an inbuilt function

string = input("Enter a String: ")
count =0
for i in string:
    count += 1

print(f"Length of String = {count}")