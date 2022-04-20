

n = int(input())
a = [int(x) for x in input().split()]

def find_max_blocks(a, n):
    blocks = []
    for i in range(n):
        for j in range(i, n):
            blocks.append((i+1, j+1))
    blocks = sorted(blocks, key=lambda x: x[1]-x[0])
    # print(blocks)
    sums = {}
    for i in range(n):
        sums[i] = {}
        sums[i][i] = a[i]
        for j in range(i+1, n):
            sums[i][j] = sums[i][j-1] + a[j]
    # print(sums)
    result = []
    for block in blocks:
        if block[1] - block[0] + 1 <= len(result):
            break
        if block in result:
            continue
        block_sum = sums[block[0]-1][block[1]-1]
        # print(block, block_sum)
        if block_sum not in sums:
            sums[block_sum] = []
        sums[block_sum].append(block)
        for sum_block in sums[block_sum]:
            if sum_block[0] <= block[0] and sum_block[1] >= block[1]:
                result.append(block)
                break
    # print(sums)
    return result

result = find_max_blocks(a, n)
print(len(result))
for r in result:
    print(r[0], r[1])