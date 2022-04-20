

# this is the "hard" version of the problem

# get the input and make it into a list
s = list(input())

# start with no characters found
found = 0

# start at the end of the string
left = len(s) - 1
right = len(s) - 1

while left >= 0:
    # if the current character is not a vowel,
    # move the right pointer back
    if s[left] not in "aeiou":
        right = left
    # if the current character is a vowel,
    # add one to the number of characters found
    else:
        found += 1
    # move the left pointer back
    left -= 1

# output the answer
print(found)
