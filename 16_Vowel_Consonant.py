# Write a program to read a character and check whether it is a vowel or a consonant.

ch = input("Enter a Character : ").lower()
vowels = ["a" , "e"  ,"i" , "o" ,"u"]
if len(ch) != 1:
    print("Enter only One Character !!")
elif ch in vowels:
    print(f"{ch} is Vowel.")
else:
    print(f"{ch} is Consonant. ")