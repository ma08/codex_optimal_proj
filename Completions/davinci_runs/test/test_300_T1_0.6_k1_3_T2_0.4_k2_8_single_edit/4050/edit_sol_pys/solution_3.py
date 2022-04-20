

n = int(input())
a = list(map(int, input().split()))

total = sum(a)

if total % n == 0:
    avg = total // n
else:
    avg = total // n + 1

# print("avg:", avg)

# find the longest subarray where sum is evenly divisible by avg
# keep track of the length of each subarray as we find it
lengths = []
sub_sum = a[0]

for i in range(n):
    if sub_sum == avg:
        lengths.append([i, i])
        sub_sum = 0
    elif sub_sum > avg:
        sub_sum -= a[i]
    sub_sum += a[i]

if sub_sum == avg:
    lengths.append([n-1, n-1])

# print("lengths:", lengths)

# create block list
blocks = []

for i in range(len(lengths)):
    for j in range(lengths[i][0], lengths[i][1]+1):
        blocks.append([j, j])

# print("blocks:", blocks)

# remove overlapping blocks
for i in range(len(blocks)):
    j = i+1
    while j < len(blocks):
        if blocks[j][0] <= blocks[i][1]: # if blocks overlap
            blocks[j][0] = blocks[i][1] + 1 # shift the right block
            if blocks[j][0] > blocks[j][1]: # if the right block is empty
                blocks.pop(j) # remove the right block
        else:
            j += 1

print(len(blocks))

for i in range(len(blocks)):
    print(blocks[i][0]+1, blocks[i][1]+1)
