# Write a program to read the marks of a student and print the grade (A/B/C/D/Fail).
marks = int(input("Enter your Marks : "))
if(marks > 100 or marks <0):
    print("INVALID MARKS !")
elif(marks>=90 ):
    print("GRADE = A")
elif(marks >=80):
   print("GRADE = B")
elif(marks>=70):
   print("GRADE = C")
elif(marks >=60):
   print("GRADE = D")
else:
    print("Fail")

