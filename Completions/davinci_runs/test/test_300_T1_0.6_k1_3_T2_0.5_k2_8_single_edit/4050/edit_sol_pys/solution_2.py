

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
lengths = [[0, 0]]
s = a[0]

for i in range(1, n):
    if s == avg:
        lengths.append([i-1, i-1])
        s = 0
    elif s > avg:
        s -= a[i-1]
    s += a[i]

if s == avg:
    lengths.append([n-1, n-1])

# print("lengths:", lengths)

# create block list
blocks = []

for i in range(len(lengths)):
    for j in range(lengths[i][0], lengths[i][1]+1):
        blocks.append([j, j])

# print("blocks:", blocks)

# remove overlapping block
for i in range(len(blocks)):
    for j in range(i+1, len(blocks)):
        if blocks[j][0] <= blocks[i][1]:
            blocks[j][0] = blocks[i][1] + 1
            if blocks[j][0] > blocks[j][1]:
                blocks.pop(j)

print(len(blocks))

for i in range(len(blocks)):
    print(blocks[i][0]+1, blocks[i][1]+1)
