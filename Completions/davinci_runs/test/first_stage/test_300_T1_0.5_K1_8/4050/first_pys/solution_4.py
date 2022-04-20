

def blocks(arr):
    blocks = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            blocks.append((i+1, j))
    return blocks

def sum_block(block, arr):
    s = 0
    for i in range(block[0]-1, block[1]):
        s += arr[i]
    return s

def find_sets(arr):
    sets = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            sets.append((i+1, j))
    return sets

def is_disjoint(b1, b2):
    return b1[0] > b2[1] or b2[0] > b1[1]

def is_valid(sets, arr):
    sums = []
    for s in sets:
        sums.append(sum_block(s, arr))
    return len(set(sums)) == 1

def is_maximal(sets, blocks, arr):
    for b in blocks:
        if b not in sets and is_disjoint(b, sets[0]) and is_disjoint(b, sets[1]) and is_valid(sets+[b], arr):
            return False
    return True

def main():
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    blocks = blocks(arr)
    sets = find_sets(arr)
    valid_sets = []
    for i in range(len(sets)):
        for j in range(i+1, len(sets)):
            if is_disjoint(sets[i], sets[j]) and is_valid(sets[i:j+1], arr) and is_maximal(sets[i:j+1], blocks, arr):
                valid_sets.append(sets[i:j+1])
    print(len(valid_sets[0]))
    for s in valid_sets[0]:
        print(s[0], s[1])

if __name__ == '__main__':
    main()