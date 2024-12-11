# Write a python script to find the number of occurrences of a particular character present in the given string using a loop. (Don’t use string methods).

a = input("Enter the string")
b = input("Enter the character")
if(not(len(b)==1)):
    print("Length of character not equal to one")
else:
    sum = 0
    for i in a :
        if i==b:
            sum=sum+1
    if (sum):
        print(f"The number of matching characters are:- {sum}")
    else:
        print("There are no such characters in the string")