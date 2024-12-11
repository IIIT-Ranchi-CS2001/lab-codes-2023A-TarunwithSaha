# For the given string S=”Ba Ba Black Sheep”, determine the following using built in functions:
# The length of the string S
# The first occurrence of the letter ‘e’
# The total number of occurrences of ‘a’
# Generate “Ta Ta Black Sheep”

S = "Ba Ba Black Sheep"
a =len(S)
print(a)
b= S.find('e')
print(b)
c =S.count('a')
print(c)
d = S.replace("Ba","Ta")
print(d)