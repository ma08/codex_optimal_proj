

# get input
s = input()
t = input()

# get length of both strings
sl = len(s)
tl = len(t)

# initialize count
count = 0

# loop through t and check if s has it
for i in range(0, sl):
    if s[i] == t[i]:
        count = count + 1

# print out result
print(sl-count)
