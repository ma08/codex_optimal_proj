

import sys

def reverse_binary(n):
    return int(bin(n)[:1:-1], 2)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(reverse_binary(n))