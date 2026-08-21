#  Write a program to print a number triangle (row i contains numbers 1 to i)

n = int(input("Enter the Range: "))

for i in range(1,n+1):

    for j in range(1,i+1):
        print(j, end ="")

    print()
