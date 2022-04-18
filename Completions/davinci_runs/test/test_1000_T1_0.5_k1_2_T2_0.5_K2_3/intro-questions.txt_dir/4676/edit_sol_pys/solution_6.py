

O = input()
E = input()

# if the length of O is larger than E, then add a space to E
if len(O) > len(E):
    E = E + " " # this will add a space to the end of E

# initialize the final password
password = ""

# for each character in O, append the character and the next character in E
for i in range(len(O)):
    password = password + O[i] + E[i]

# print the password
print(password)
