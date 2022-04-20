

# this is the "easy" version of the problem
# the "hard" version has a longer string

# get the input 
s = input()
t = input()

# start with no characters removed
removed = 0

# start at the beginning of the string
left = 0
right = 0

# go until the end of the string
while right < len(s):
    # if the current character is in the target string,
    # move the left pointer up to the current spot
    if s[right] in t:
        left = right
    # if the current character is not in the target string,
    # add one to the number of characters removed
    else:
        removed += 1
    # move the right pointer up
    right += 1

# output the answer
print(removed)
