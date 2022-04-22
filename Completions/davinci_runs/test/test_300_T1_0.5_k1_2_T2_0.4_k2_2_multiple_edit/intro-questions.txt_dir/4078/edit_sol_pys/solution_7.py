

import argparse
import os
import sys
import logging
from collections import defaultdict
from typing import List

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.disable(logging.CRITICAL)


def main(args):
    lines = args.input_file.readlines()
    n, k = map(int, lines[0].split())
    a = list(map(int, lines[1].split()))[:n]
    b = list(map(int, lines[2].split()))[:n]

    a.sort()
    b.sort()

    for i in range(k):
        if a[i] < b[n - i - 1]:
            a[i], b[n - i - 1] = b[n - i - 1], a[i]
        else:
            break

    res = sum(a)

    with open(args.output_file, "w") as f:
        f.write(str(res) + "\n")

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("-o", "--output_file", type=str, default=sys.stdout)
    args = parser.parse_args()

    main(args)
