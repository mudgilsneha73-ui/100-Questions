# Write a program to reverse a string.
word = input("Enter the String: ")

reverse = ""
for i in range(len(word) -1,-1,-1):
    reverse += word[i] 

print(reverse) 
