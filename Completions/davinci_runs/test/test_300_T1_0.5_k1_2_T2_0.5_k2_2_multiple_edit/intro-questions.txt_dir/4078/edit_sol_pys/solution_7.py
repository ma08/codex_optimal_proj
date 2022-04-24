

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
    n = int(lines[0])
    b = list(map(int, lines[2].split()))[:n]
    c = list(map(int, lines[3].split()))[:n - 1]

    # print(a)
    # print(b)
    # print(c)

    dp = [0] * n
    dp[0] = a[0]
    for i in range(1, n):
        dp[i] = min(dp[i - 1] + a[i], dp[i - 1] + b[i])
        if i > 1:
            dp[i] = min(dp[i], dp[i - 2] + b[i] + c[i - 1])

    # print(dp)
    a = list(map(int, lines[1].split()))[:n]

    max_diff = 0
    for i in range(n):
        max_diff = max(max_diff, dp[i])

    with open(args.output_file, "w") as f:
        f.write(str(max_diff))

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("-o", "--output_file", type=str, default=sys.stdout)
    args = parser.parse_args()

    main(args)
