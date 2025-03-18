import random
import string


pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)


#list comprehension [function for i in range(n)]

res = "".join([random.choice(charValues) for i in range(pass_len)])

print(res)

#print("your random password is: ", password)