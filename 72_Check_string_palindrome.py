#  Write a program to check whether a string is a palindrome

word = input("Enter the word: ")

org = word
reverse = ""

for i in range(len(word) -1,-1,-1):
    reverse += word[i] 

if org ==  reverse:
    print(f"{word} is Palindrome ")
else:
    print(f"{word} is not Palindrome")
