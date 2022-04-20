

# get input from user
a = input()
b = input()

# get length of both input
al = len(a)
bl = len(b)

# initialize count
count = 0

# loop through b and check if a has it
for i in range(0, bl):
    if a[i] != b[i]:
        count += 1

# print out result
print(count)
