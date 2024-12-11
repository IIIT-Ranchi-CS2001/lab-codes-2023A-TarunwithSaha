# Write a python program to find 
#(a) Area and Perimeter of Triangle when all the sides are given (take user's i/p). Hint: Use Heron's Eq.
import math
a = float(input("Enter the length of first side of a triangle "))
b = float(input("Enter the length of second side of a triangle "))
c = float(input("Enter the length of third side of a triangle "))
p = a+b+c
s = p/2.0
a = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The perimeter and area of the triangle are :-")
print(p)
#print(" ")
print(a)
print("respectively.")
#(b) Find all three angles of the above triangle 
#-> Display i/p and o/p

# to find an angle of the triangle , the formula is :- degrees(arcos(b**2+c**2-a**2)/(2*b*c)) for angle A whoseadjacent sides are b , c and opposite side is a.

A = math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
B = math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
C = math.degrees(math.acos((b**2+a**2-c**2)/(2*b*a)))

print(A)
print(B)
print(C)
