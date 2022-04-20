

import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    #print(n)
    #print(a)
    #print(len(a))
    if n != len(a):
        sys.exit(-1)
    if n > 1500:
        sys.exit(-1)

    # first find the sums of each block
    # a list of tuples of form (sum, start, end)
    sums = []
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += a[j]
            if (sum, i, j) not in sums:
                sums.append((sum, i, j))
    #print(sums)

    # now we need to find the max number of blocks
    # we can do this by seeing what the max number of sums is
    sums.sort()
    #print(sums)
    max = 0
    for i in range(len(sums)):
        if sums[i][0] == sums[i+1][0]:
            max += 1
    #print(max)

    # now we need to find the blocks in the array
    # we can do this by iterating through the sums
    # and printing the block if it's a valid block
    # and doesn't overlap with any previous blocks
    blocks = []
    for i in range(len(sums)):
        if (sums[i][1], sums[i][2]) not in blocks:
            blocks.append((sums[i][1], sums[i][2]))
        if len(blocks) == max:
            break
    #print(blocks)

    # now we need to print the output
    print(len(blocks))
    for i in range(len(blocks)):
        print(str(blocks[i][0] + 1) + " " + str(blocks[i][1] + 1))

if __name__ == '__main__':
    main()