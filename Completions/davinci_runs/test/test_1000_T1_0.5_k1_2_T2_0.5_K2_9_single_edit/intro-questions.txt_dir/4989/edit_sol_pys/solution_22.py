

import sys

def main():
    n = int(sys.stdin.readline())
    pieces = [int(x) for x in sys.stdin.readline().split()]
    pieces.sort()
    alice = 0
    bob = 0
    for i in range(n):
        if i % 2 == 0:
            alice += pieces[n-i-1]
        else:
            bob += pieces[n-i-1]
    print(alice - bob)

if __name__ == "__main__":
    main()
