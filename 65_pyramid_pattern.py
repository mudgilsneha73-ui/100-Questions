# Write a program to print a pyramid pattern of stars of height n

n = int(input("Enter the Height: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()