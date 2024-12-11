# Write a python script to find the squares of first n natural numbers. Display both the number and the square as shown below. Use while loop
# Number    	Square
# 1              	1
# 2               	4
# …		…
# n		n

def sq(n):
    print("Number               Square")
    for i in range(1,n+1):
        print(i,end="                      ")
        print(i*i,end="                    ")
        print()
n = int (input("Enter the natural number n:-"))
sq(n)