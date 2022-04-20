

# solution

# input
s = input()

# convert to list
s = list(s)

# initialize count
count = 0

# loop through list
for i in range(len(s)):
    # if the number is divisible by 3, add 1 to count
    if int(s[i]) % 3 == 0:
        count += 1

#print count
print(count)
