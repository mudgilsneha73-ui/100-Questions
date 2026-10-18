# Write count_vowels(s) that returns the number of vowels in a string.

# count_vowels("education")  -> 5

def count_vowels(s):
    count = 0
    for ch in s:
        if ch in "aeiou":
            count += 1
    return count

print(count_vowels("education"))   # 5
print(count_vowels("education"))   # 5  
print(count_vowels("Python"))      # 1
