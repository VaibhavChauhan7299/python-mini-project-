# import random
# import string

# #print(string.ascii_letters)
# #print(string.digits)
# #print(string.punctuation)

# #val = random.choice(['a', 'b', 'c', 'd',])
# #print(val)

# pass_len = 14
# charValues = string.ascii_letters + string.digits + string.punctuation

# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)

# print("your random password is:", password)

# #list comprehension [function for i in range(n)]

# res = "".join([random.choice(charValues)for i in range(pass_len)])
# print(res)