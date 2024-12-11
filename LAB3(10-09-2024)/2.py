# Write a python script to find the sum of the digits of the given number using a while loop. Display the number and the sum.

def sum(n):
    sum=0
    n1=n
    while(n1):
        sum=sum+(n1%10)
        n1//=10
    print(n ,end=" ")
    print(sum)
a =int(input("Enter the number:-"))
sum(a)