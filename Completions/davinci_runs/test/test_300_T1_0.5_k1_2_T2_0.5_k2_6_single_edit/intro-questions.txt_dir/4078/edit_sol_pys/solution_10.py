

import argparse
import os
import sys
from itertools import combinations
import logging
from collections import defaultdict
from typing import List

logging.basicConfig(level=logging.INFO, format="%(message)s")
# logging.disable(logging.CRITICAL)


def main(args):
    lines = args.input_file.readlines()
    n, m = map(int, lines[0].split())
    a = list(map(int, lines[1].split()))
    segments = []
    for i in range(m):
        segments.append(tuple(map(int, lines[i + 2].split())))

    max_diff = -1
    max_indices = None
    for indices in combinations(range(m), m // 2):
        diff = sum(sum(a[l - 1:r]) for i, (l, r) in enumerate(segments) if i not in indices)

        if diff > max_diff:
            max_diff = diff
            max_indices = [i + 1 for i in indices]

    with open(args.output_file, "w") as f:
        f.write(str(max_diff) + "\n")
        f.write(str(len(max_indices)) + "\n")
        f.write(" ".join(map(str, max_indices)) + "\n")

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("-o", "--output_file", type=str, default=sys.stdout)
    args = parser.parse_args()

    main(args)
