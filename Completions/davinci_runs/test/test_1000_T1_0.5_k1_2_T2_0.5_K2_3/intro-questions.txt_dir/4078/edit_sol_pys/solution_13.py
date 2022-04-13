

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
    logging.info(lines)

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("-o", "--output_file", type=str, default=sys.stdout)
    args = parser.parse_args()

    main(args)
