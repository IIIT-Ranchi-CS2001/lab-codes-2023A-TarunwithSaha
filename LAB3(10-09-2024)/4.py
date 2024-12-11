# Write a python script to print the multiplication table of a given number up to the specified limit using a for loop.

n = int(input("Enter the nummber :-"))
n1 = int(input("Enter the limit :-"))

def table(n,n1):
    for i in range (1,n1+1):
        print(f"{n} * {i} = {n*i} ")
table(n,n1)