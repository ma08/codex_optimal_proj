

# this is a "hard" version of the problem
# the "easy" version has a shorter string

# get the input and split it into an array
inputs = input().split()

# get the string and the target
s = inputs[0]
t = inputs[1]

# start with an empty string
answer = ""

for i in range(len(s)):
    # if the current character is not in the target string
    if s[i] not in t:
        # add it to the answer
        answer += s[i]
    # if the current character is in the target string
    else:
        # add a space to the answer
        answer += " "

# output the answer
print(answer)
