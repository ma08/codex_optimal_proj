

# input
N = int(input())

# initialize
count = 0

# loop
for i in range(1, N + 1):
    if '3' in str(i) and '5' in str(i) and '7' in str(i):
        count += 1

# output
print(count)