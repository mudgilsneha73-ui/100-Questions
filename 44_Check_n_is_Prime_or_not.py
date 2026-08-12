# Write a program to read a number and check whether it is prime or not

n = int(input("Enter the Value of n: "))

if n <= 1:
    print(f"{n} is not a Prime number")
else:
    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{n} is a Prime number")
    else:
        print(f"{n} is not a Prime number")