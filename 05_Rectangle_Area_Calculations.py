# Write a program to read the length and breadth of a rectangle and print its area and perimeter.

length = int(input("Enter the Length of Rectangle: "))
breadth = int(input("Enter the Breadth of Rectangle: "))

area = length * breadth

perimeter = 2 * (length + breadth)

print(f"Area of Rectangle = {area}")
print(f"Perimeter of Rectangle = {perimeter}")
