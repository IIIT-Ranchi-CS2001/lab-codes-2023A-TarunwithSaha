# Write a program to find the roots of a quadratic equation when the coefficients a, b and c are given ( assume that a, b and c are integers)
# Hint: find the discriminant d= b2 − 4ac
# If d = 0, the equation has one real repeated root (both roots are the same: 
# R1= R2 = -b/(2a)

# If d > 0, the equation has two distinct real roots.
# 	R1= (-b + sqrt(d))/2a
# R2= (-b - sqrt(d))/2a
 
# If d < 0, the equation has two complex roots.
# real_part = -b / (2 * a) 
# imaginary_part = math.sqrt(-discriminant) / (2 * a)

import math
print("Enter the values of a, b, c:-")
a =int(input("Enter the value of a:-"))
b= int(input("Enter the value of b:-"))
c= int(input("Enter the value of c:-"))
d= b**2-4*a*c
if(d==0):
    r1 =(-b)/(2*a)
    r2=r1
    print("Root 1:-")
    print(r1)
    print("Root 2:-")
    print(r2)
elif(d>0):
    r1= (-b + math.sqrt(d))/(2*a)
    r2= (-b - math.sqrt(d))/(2*a)
    print("Root 1:-")
    print(r1)
    print("Root 2:-")
    print(r2)
elif(d<0):
    m1 = -b / (2 * a) 
    n1 = math.sqrt(-d) / (2 * a)
    n2 = -1*(math.sqrt(-d) / (2 * a))
    r1=complex(m1,n1)
    r2=complex(m1,n2)
    print("Root 1:-")
    print(r1)
    print("Root 2:-")
    print(r2)