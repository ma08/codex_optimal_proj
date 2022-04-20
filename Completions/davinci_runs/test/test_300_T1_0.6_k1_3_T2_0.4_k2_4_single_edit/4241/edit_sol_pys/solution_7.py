

# get input from user
s = raw_input()
t = raw_input()

# get length of both strings and initialize count
sl = len(s) 
tl = len(t) 
count = 0 

# loop through t and check if s has it, if not increment count
for i in range(0, tl):
    if s[i] != t[i]:
        count += 1

# print out result, the number of differences between the two strings
print str(count)
