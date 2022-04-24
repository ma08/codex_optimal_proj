

# get input
s = input("")
t = input("")

# get length of both strings
sl = len(s)
tl = len(t)

# initialize count
count = 0

# loop through t and check if s has it
for i in range(0, tl):
    if s[i] != t[i]:
        count += 1

# print out result
print(count)
