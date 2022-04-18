

import sys

def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    input()
    a = sorted(list(map(int, input().split())))
    alice = 0
    bob = 0
    while len(a) > 0:
        alice += a.pop()
        if len(a) > 0:
            bob += a.pop()
    print(alice, bob)

if __name__ == "__main__":
    main('broken')
