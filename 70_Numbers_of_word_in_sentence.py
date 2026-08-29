#  Write a program to count the number of words in a sentence.
sentence = input("Enter a sentence: ")
count = 0
word = sentence.split()

for i in word:
    count += 1

print(f"Numbers in this Sentence is {count}")

