#Write A Program to take input temprature from user and convert it into fahrenhit 
#Display i/p temp and o/p
#F= C*1.8+32

a = float(input("Enter the temperature in celsious"))
b= (a*1.8)+32
print("The temperature in celcious is :-")
print(a)
print("The temperature in fahrenhit is :-")
print("%.2f" % b)

# The code to print the ans to two decimal places:- "%.2f" % <variable>