

from collections import defaultdict
from typing import List

import sys
def solve(words: List[str]) -> int:
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1

    word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    if word_counts[0][1] < 2:
        return len(words)

    return len(words) - (word_counts[0][1] - 1) * (len(word_counts[0][0]) - 1)


if __name__ == '__main__':
    _ = sys.stdin.readline()
    words = sys.stdin.readline().split()
    print(solve(words))
