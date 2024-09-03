#If the given string S1= “Maha Bharat”, generate the following strings by manipulating S1.
# “mAHA bHARAT”
# “Bharat”
# “BharatBharatBharat”
# “Mera Bharat”
# “Mera Bharat Mahan”

S1 = "Maha Bharat"
S2 = S1.swapcase()
print(S2)
S3=S1[5:]
print(S3)
print(S3*3)
S4=S1.replace("Maha","Mera")
print(S4)
S5=S4+" Mahan"
print(S5)
