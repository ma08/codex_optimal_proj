

from collections import defaultdict
from typing import List, Tuple


def solve(words: List[str]) -> int:
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1

    word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)  # type: List[Tuple[str, int]]

    if word_counts[0][1] < 2:
        return len(words)

    return len(words) - (word_counts[0][1] - 1) * (len(word_counts[0][0]) - 1)


if __name__ == '__main__':
    _ = input()
    words = input().split()
    print(solve(words))
