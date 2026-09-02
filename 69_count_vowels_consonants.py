#  Write a program to count the number of vowels and consonants in a string.
string = input("Enter the String: ")
vowel = 0
consonants = 0
vowels = {"a","e","i","o","u"}

for i in string:
    if i.lower() in vowels:
        vowel += 1

    elif i.isalpha:
        consonants += 1
    

print(f"Vowel = {vowel} and Consonants = {consonants}")