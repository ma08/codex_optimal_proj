
# Get input
s = input()
t = input()

# Get length of both strings
sl = len(s)
tl = len(t)

# Initialize count
count = 0

# Loop through t and check if s has it
for i in range(0, tl):
    if s[i] != t[i]:
        count += 1

# print out result
print(count)
