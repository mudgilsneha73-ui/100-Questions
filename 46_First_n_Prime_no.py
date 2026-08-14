#   Write a program to display the first n prime numbers
n = int(input("Enter the value of n: "))

count = 0
i = 2
while count < n:
    prime = True
    for j in range(2,i):
      if(i % j == 0):
        prime = False
        break 
    if prime:

        print(i)
        count += 1
    i += 1


    