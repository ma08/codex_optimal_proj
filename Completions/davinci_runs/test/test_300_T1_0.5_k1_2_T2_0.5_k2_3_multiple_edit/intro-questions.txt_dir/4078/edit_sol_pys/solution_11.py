

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
    n, m = map(int, lines[0].split())
    a = list(map(int, lines[1].split()))
    segments = []
    for i in range(1, m + 1):
        segments.append(tuple(map(int, lines[i].split())))

    max_diff = 0
    max_index = None
    for i in range(m):
        diff = 0
        index = None
        for j in range(m):
            if j == i:
                continue

            l, r = segments[j]
            diff += sum(a[l - 1:r])
            index = j + 1
        if diff > max_diff:
            max_diff = diff
            max_index = index

    with open(args.output_file, "w") as f:
        f.write(str(max_diff) + "\n")
        f.write(str(max_index) + "\n")

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("-o", "--output_file", type=str, default=sys.stdout)
    args = parser.parse_args()

    main(args)
