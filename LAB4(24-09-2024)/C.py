# Generate 2 lists (course code and course name). create a new list with both course code and name like["CS1001:Python",...]

a = []
b= []
c=[]
n=int(input("Enter the number of subjects:-"))
for i in range (1,n):
    x=input("Enter the course code:-")
    y=input("Enter the course name:-")
    a.append(x)
    b.append(y)
    c.append(x+":"+y)
print(c)
