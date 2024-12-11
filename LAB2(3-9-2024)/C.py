# Write a python script to enter any string at run time and check whether it is a palindrome or not.

a = input("Enter a String to check if it is palindrome:-")
b=a.lower()

c = b[::-1]
if (b==c):
    print("Palindrome")
else:
    print("Not a Palindrome")
# for i in range(1,b/2):
#     for j in 