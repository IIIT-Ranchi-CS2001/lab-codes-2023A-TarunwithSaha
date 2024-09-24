# // Find the number of palindrome words in the given sentence without defining any new function (feel free to use python’s in-built functions).

a = input("Enter the string:-")
b=a.split()
c=0
for i in b:
    if(i[::]==i[::-1]):
        c+=1
print(c)