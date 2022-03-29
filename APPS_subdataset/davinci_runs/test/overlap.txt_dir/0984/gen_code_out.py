

import sys

def main():
    n = int(sys.stdin.readline())
    tree = {}
    for i in range(n):
        v, l, r = map(int, sys.stdin.readline().split())
        tree[i] = (v, l, r)
    print(count_fails(tree))

def count_fails(tree):
    fails = 0
    for i in range(len(tree)):
        fails += count_fails_for_node(tree, i)
    return fails

def count_fails_for_node(tree, i):
    v, l, r = tree[i]
    if l == -1 and r == -1:
        return 0
    if l == -1:
        return count_fails_for_node(tree, r)
    if r == -1:
        return count_fails_for_node(tree, l)
    return count_fails_for_node(tree, l) + count_fails_for_node(tree, r) + 1

if __name__ == '__main__':
    main()