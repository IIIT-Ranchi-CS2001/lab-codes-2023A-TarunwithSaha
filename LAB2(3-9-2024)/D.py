# Enter the following details of a student at run time: - Name, Roll number and marks secured for Mathematics Examination out of 100. Write a python script to display student details as shown:
# Name:
# Roll Number:
# Marks:
# Grade Point:
# Remark:
# The criteria for awarding grade point and remark are as given in the table:

# S. No.
# Range of Marks
# Grade Point
# Remark
# 1
# >= 90
# 10
# OUTSTANDING
# 2
# 90 > Marks >= 80
# 9
# VERY GOOD
# 3
# 80 > Marks >= 70
# 8
# GOOD
# 4
# 70 > Marks >= 60
# 7
# AVERAGE
# 5
# 60 > Marks >= 50
# 6
# PASS
# 6
# Marks < 50
# 0
# FAIL

name = input("Enter your name")
roll =input("Enter the roll number")
marks = int(input("Enter your marks"))
if (marks>=90):
    grade =10
    remarks ="Outstanding"
elif(marks<90 and marks>=80):
    grade = 9
    remarks ="Very Good"
elif (marks<80 and marks>=70):
    grade = 8
    remarks ="Good"
elif (marks<70 and marks>=60):
    grade =7
    remarks ="Average"
elif (marks <60 and marks >=50):
    grade =6
    remarks ="Pass"
elif (marks<50):
    grade =0
    remarks="Fail"
print("Name:")
print(name)
print("Roll number:")
print(roll)
print("Marks:")
print(marks)
print("Grade Point:")
print(grade)
print("Remark:")
print(remarks)