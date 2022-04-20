

# get the input
s = input()
t = input()

# remove all instances of the target string
s = s.replace(t, "")

# start with no characters removed
removed = 0

# go through the string
for c in s:
    # add one to the number of characters removed
    removed += 1

# output the answer
print(removed)
