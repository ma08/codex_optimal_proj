

import os
import sys
import csv
import re
import datetime


def main(argv):
    if len(argv) != 2:
        print("Usage: python3 %s <input_file>" % argv[0])
        sys.exit(1)

    input_file = argv[1]
    if not os.path.isfile(input_file):
        print("Error: File '%s' does not exist" % input_file)
        sys.exit(2)

    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


if __name__ == "__main__":
    main(sys.argv)
