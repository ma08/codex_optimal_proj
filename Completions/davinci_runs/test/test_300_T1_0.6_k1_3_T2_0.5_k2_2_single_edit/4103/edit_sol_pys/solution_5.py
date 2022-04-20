

import sys

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        a, b = [int(i) for i in sys.stdin.readline().strip().split(' ')]
        s = a + b
        print(s)

main()
