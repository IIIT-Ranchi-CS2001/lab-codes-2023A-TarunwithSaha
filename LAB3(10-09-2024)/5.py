# Write a python script to check whether all the characters present in a string are alphanumeric (uppercase letters, lowercase letters or digits) using for  with else. Print True if all characters are alphanumeric. Otherwise print False.

a = input("Enter the string:-")
for j in a:
    i=ord(j)
    # print(i)
    if(not(i>=65 and i<=90) and not(i>=97 and i<=122) and not(i>=48 and i<=57) ):
        print("False")
        break
else :
    print("True")
