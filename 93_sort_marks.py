''' Sort this list by marks, highest first:

students = [("Ravi", 82), ("Sita", 91), ("Amit", 76)]
-> [('Sita', 91), ('Ravi', 82), ('Amit', 76)] '''

key = lambda students :students[1]

students = [("Ravi", 82), ("Sita", 91), ("Amit", 76)]

print(sorted(students,key = key, reverse = True))
