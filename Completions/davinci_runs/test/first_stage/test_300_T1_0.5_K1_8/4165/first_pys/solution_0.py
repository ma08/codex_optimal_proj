

import sys

def main():
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    l.sort()
    if l[-1] < sum(l[:-1]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()