# Generate two sets – first for all singers and second for all dancers of the class using set comprehension. Perform set operations to generate the following sets 
# of all artists of the class
# allrounders of the class
# dancers but not singers
# singers but not dancers
# dancers but not singers cum singers but not dancers


Singers=set()
Dancers=set()

s= int(input("Enter the number of singers:-"))
d= int(input("Enter the number of dancers:-"))

for i in range(1,s):
    x=input("Enter the name of singer:-")
    Singers.add(x)
for j in range(1,d):
    y=input("Enter the name of dancers:-")
    Dancers.add(y)
artists = set()
all_rounders = set()
D_butnot_S = set()
S_butnot_D = set()
D_b_S_A_S_b_D = set()
print('artists')
artists= Singers | Dancers
print(artists)
print('all_rounders')
all_rounders = Singers&Dancers
print(all_rounders)
print('D_butnot_S')
D_butnot_S = Dancers - Singers
print(D_butnot_S)
print('S_butnot_D')
S_butnot_D = Singers - Dancers
print(S_butnot_D)
print('D_b_S_A_S_b_D')
D_b_S_A_S_b_D  =  D_butnot_S | S_butnot_D
print(D_b_S_A_S_b_D)
# print(artists)
# print(all_rounders)
# print(D_butnot_S)
# print(S_butnot_D)
# print(D_b_S_A_S_b_D)