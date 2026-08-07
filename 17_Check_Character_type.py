'''
Write a program to read a character and check whether it is an alphabet, digit or special
 symbol 
 '''

ch = input("Enter the Character : ")
if len(ch) != 1:
    print("Enter only One Character !!")
elif ch.isalpha():
    print(f"{ch} is Alphabet.")
elif ch.isdigit():
    print(f"{ch} is Digit.")
else:
    print(f"{ch} is Special Symbol.")