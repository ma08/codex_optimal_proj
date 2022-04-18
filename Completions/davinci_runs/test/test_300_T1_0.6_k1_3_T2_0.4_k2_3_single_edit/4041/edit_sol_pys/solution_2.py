

# get the input
n = int(input())
s = input()

# initialize the answer
answer = 0

# loop through the characters in the string
for i in range(n):
    # if the current character is a vowel
    if s[i] in "aeiou":
        # add the number of characters after this one
        # to the answer
        answer += n - i

# output the final answer
print(answer)
