# -*- coding: utf-8 -*-

import re
import sys

def main():
    S = sys.stdin.read().rstrip()
    result = re.findall('A+|C+|G+|T+', S)
    print(max(result, key=len))

if __name__ == '__main__':
    main()
