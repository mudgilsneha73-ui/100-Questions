#  Write a program to print a right-angled triangle pattern of stars of height n.

n = int(input("Enter the value of n: "))

for i in range(1, n+1):

   for j in range(i):
        print("*", end="")
        
   print()    
