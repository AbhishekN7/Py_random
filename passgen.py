import string
import random

s1= string.ascii_uppercase
s2= string.ascii_lowercase
s3= string.punctuation
s4= string.digits

passlen=int(input("Enter the Length of Password:\n"))

str=[]
str.extend(list(s1))
str.extend(list(s2))
str.extend(list(s3))
str.extend(list(s4))

# print("".join(str[0:passlen]))

print("Here is your Password:\n")
print("".join(random.sample(str,passlen)))

