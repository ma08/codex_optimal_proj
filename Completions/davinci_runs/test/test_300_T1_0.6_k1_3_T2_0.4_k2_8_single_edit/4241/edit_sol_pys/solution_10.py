

# get input and convert to int
n = int(input())
k = int(input())

# initialize sum
sum = 0
# loop through numbers
for i in range(1, n + 1):
    # check if i is divisible by k
    if i % k == 0:
        sum += i

# print out result
print(sum)
