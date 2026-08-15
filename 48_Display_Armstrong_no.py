# Write a program to display all Armstrong numbers from 1 to n.

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):

    original = i
    count = 0

    # Count digits
    temp = i
    while temp != 0:
        digit = temp % 10
        count += 1
        temp = temp // 10

    # Calculate Armstrong sum
    total = 0
    temp = i

    while temp != 0:
        digit = temp % 10
        total += digit ** count
        temp = temp // 10

    if total == original:
        print(f"{original} is an Armstrong number.")


