

import sys

def get_blocks(lst):
    blks = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            blks.append((i+1, j+1))
    return blks

def get_sum(lst, blk):
    return sum(lst[blk[0]-1:blk[1]])

def get_disjoint_blocks(lst):
    blks = get_blocks(lst)
    sums = {}
    for blk in blks:
        sum_blk = get_sum(lst, blk)
        if sum_blk in sums:
            sums[sum_blk].append(blk)
        else:
            sums[sum_blk] = [blk]
    return sums

def get_max_disjoint_blocks(lst):
    disjoint_blks = get_disjoint_blocks(lst)
    max_len = 0
    max_blks = []
    for sum_blks in disjoint_blks.values():
        if len(sum_blks) > max_len:
            max_len = len(sum_blks)
            max_blks = sum_blks
    return max_blks

def main():
    n = int(sys.stdin.readline().strip())
    lst = list(map(int, sys.stdin.readline().strip().split()))
    assert(len(lst) == n)
    max_blks = get_max_disjoint_blocks(lst)
    print(len(max_blks))
    for blk in max_blks:
        print(blk[0], blk[1])

if __name__ == '__main__':
    main()