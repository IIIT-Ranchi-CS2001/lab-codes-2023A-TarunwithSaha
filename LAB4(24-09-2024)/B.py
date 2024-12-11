# Create a list of int using list comprehension [multiple input from keyboard].  Find the mean, median, and mode of the given list (usage of specific modules such as statistics is strictly prohibited. Lab problems are for you to build-up logic and strengthen your understanding of the topic & its concepts).

l=[]
n = int(input("Enter the number of elements in l "))
n+=1
for i in range(1,n):
    x=int(input("Enter an element:-"))
    l.append(x)
mean= sum(l)/n
