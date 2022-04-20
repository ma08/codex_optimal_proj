

# get the input
n = int(input())
s = input()

# start with no flips
flips = 0

# go through each character in the string
for i in range(n):
    # if the character is not a '+', add one to the flip count
    if s[i] != '+':
        flips += 1

# output the answer
print(flips)
