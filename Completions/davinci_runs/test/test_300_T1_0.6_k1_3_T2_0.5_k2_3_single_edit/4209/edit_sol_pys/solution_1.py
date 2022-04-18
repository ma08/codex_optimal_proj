
# Solution for https://codeforces.com/problemset/problem/1238/C

def is_valid_block(block):
    return block[0] <= block[1]

def get_sum(block, arr):
    return sum(arr[block[0]-1:block[1]])

def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    blocks = [(i, j) for i in range(1, n+1) for j in range(i, n+1)]
    blocks = [block for block in blocks if is_valid_block(block)]
    blocks = [(i, block) for i, block in enumerate(blocks)]
    blocks = sorted(blocks, key=lambda x: get_sum(x[1], arr))
    blocks = [(block[0]+1, block[1]) for _, block in blocks]

    blocks = [blocks[0]]
    for i in range(1, len(blocks)):
        if get_sum(blocks[i], arr) == get_sum(blocks[i-1], arr):
            blocks[i] = (blocks[i-1][0], blocks[i][1])
        else:
            blocks.append(blocks[i])

    print(len(blocks))
    for block in blocks:
        print(block[0], block[1])

main()
