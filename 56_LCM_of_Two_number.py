# Write a program to find the LCM of two numbers.

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))   

multiply = 1
for i in range(1, n+1):
    multiply = m * i

    if multiply % n == 0:
        print(multiply)
        break
  
  
   
     


      
