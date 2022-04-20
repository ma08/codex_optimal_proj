

# get input
s = input().split()
t = input().split()

# get length of both strings
sl = int(s[0])
tl = int(t[0])

# initialize count
count = 0

# loop through t and check if s has it
for i in range(0, tl):
    if s[i+1] != t[i+1]:
        count += 1

# print out result
print(count)
