import os

import hashlib
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if line.startswith("#"):
            continue
        if not os.path.isfile(line):
            continue
        print(hash_file(line))

def hash_file(filename):
    with open(filename) as f:
        return hashlib.sha256(f.read()).hexdigest()

if __name__ == "__main__":
    main()
