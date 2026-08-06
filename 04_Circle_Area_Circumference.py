# Write a program to read the radius of a circle and print its area and circumference.
import math

r = float(input("Enter the radius of circle: "))

area = math.pi * r * r
circumference = 2 * math.pi * r

print(f"Area of Circle = {area}")
print(f"Circumference of circle = {circumference}")

