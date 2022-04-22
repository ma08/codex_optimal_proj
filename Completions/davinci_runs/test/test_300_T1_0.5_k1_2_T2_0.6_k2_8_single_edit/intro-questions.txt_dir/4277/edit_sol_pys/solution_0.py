#include <iostream>

import sys

def main():
    n, a, b = map(int, sys.stdin.readline().split())
    print(min(n*a, b))

main()
