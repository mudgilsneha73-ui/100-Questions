#  Write a program to print an inverted right-angled triangle pattern of stars of height n.

n = int(input("Enter the value of n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()                                                                                                          