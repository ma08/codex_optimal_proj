

from sys import stdin
from collections import defaultdict
from itertools import combinations
from math import inf

def main():
    n = int(stdin.readline())
    words = stdin.readline().split()
    # print(n, words)
    lengths = [len(w) for w in words]
    # print(lengths)
    total_length = sum(lengths)
    # print(total_length)
    # print(list(combinations(range(n), 2)))
    # print()
    min_length = inf
    for i, j in combinations(range(n), 2):
        # print(i, j)
        if words[i] == words[j]:
            k = i + 1
            while k < j and words[k] == words[i]:
                k += 1
            # print(i, j, k)
            if k == j:
                # print(words[i], k - i)
                # print(total_length - (k - i) * lengths[i] + len(words[i].upper()))
                min_length = min(min_length, total_length - (k - i) * lengths[i] + len(words[i].upper()))
    print(min_length if min_length != inf else total_length)

main()