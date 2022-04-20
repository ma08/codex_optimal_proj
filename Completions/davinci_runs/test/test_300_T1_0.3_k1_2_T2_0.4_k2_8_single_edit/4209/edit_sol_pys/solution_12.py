

def get_blocks(n, a):
    blocks = []
    for i in range(n):
        for j in range(i, n):
            blocks.append((i, j))
    return blocks

def get_block_sum(a, block):
    return sum(a[block[0]:block[1]+1])

def get_block_set(a, blocks):
    block_set = []
    for block in blocks:
        if block not in block_set:
            block_set.append(block)
            for i in range(block[0]+1, block[1]):
                for j in range(i, block[1]):
                    if (i, j) in block_set:
                        block_set.remove((i, j))
    return block_set

def get_block_set_sum(a, block_set):
    return sum(get_block_sum(a, block) for block in block_set)

def get_max_block_set(a, blocks):
    max_block_set = []
    max_block_set_sum = 0
    for block in blocks:
        block_set = get_block_set(a, [block])
        block_set_sum = get_block_set_sum(a, block_set)
        if block_set_sum > max_block_set_sum:
            max_block_set = block_set
            max_block_set_sum = block_set_sum
    return max_block_set

def main():
    n = int(input())
    a = list(map(int, input().split()))
    blocks = get_blocks(n, a)
    max_block_set = get_max_block_set(a, blocks)
    print(len(max_block_set))
    for block in max_block_set:
        print(block[0]+1, block[1]+1)

if __name__ == '__main__':
    main()
