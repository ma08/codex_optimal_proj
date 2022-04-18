import math
import os
import random
import re
import sys

import sys

def main():
    n = int(sys.stdin.readline())
    print(int(bin(n)[:1:-1], 2))

if __name__ == "__main__":
    main()
