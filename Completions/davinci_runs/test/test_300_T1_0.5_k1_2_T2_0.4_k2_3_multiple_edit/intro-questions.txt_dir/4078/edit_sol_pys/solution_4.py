

import argparse
import os
import sys
import logging
from collections import defaultdict
from typing import List

logging.basicConfig(level=logging.INFO, format="%(message)s")
# logging.disable(logging.CRITICAL)


def main(args):
    lines = args.input_file.readlines()
    n, m = map(int, lines[0].split())  # type: int, int
    a = list(map(int, lines[1].split()))  # type: List[int]
    segments = []
    for i in range(m):
        segments.append(tuple(map(int, lines[i + 2].split())))  # type: List[Tuple[int, int]]

    max_diff = 0  # type: int
    max_indices = set()  # type: Set[int]
    for i in range(m):
        diff = 0  # type: int
        indices = set()  # type: Set[int]
        for j in range(m):
            if j == i:
                continue

            l, r = segments[j]  # type: int, int
            diff += sum(a[l - 1:r])
            indices.add(j + 1)
        if diff > max_diff:
            max_diff = diff
            max_indices = indices

    with open(args.output_file, "w") as f:
        f.write(str(max_diff) + "\n")
        f.write(str(len(max_indices)) + "\n")
        f.write(" ".join(map(str, max_indices)) + "\n")

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("-o", "--output_file", type=str, default="output.txt")
    args = parser.parse_args()

    main(args)
