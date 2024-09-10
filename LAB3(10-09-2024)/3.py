# Write a python script to print the first n terms of the Fibonacci series using while loop
def f(n):
    print("1 1",end =" ")
    a=1
    b=1
    sum=a+b
    n1=n-2
    while(n1):
        print(sum,end=" ")
        n1=n1-1
        a=b
        b=sum
        sum=a+b


n = int (input("Enter the number :-"))
f(n)
