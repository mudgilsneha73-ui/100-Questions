# Write a program to convert a string to uppercase and lowercase without inbuilt case functions

word = input("Enter the word: ")

lowercase = ""
uppercase = ""

 
for i in word: 
    n = ord(i)
    if n >= 65 and n <= 90:
        lowercase += chr(n+32)
    elif n >= 97 and n <= 122:
        uppercase += chr(n- 32)


print(lowercase)
print(uppercase)

