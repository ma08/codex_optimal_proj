

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    p = list(map(int, sys.stdin.readline().rstrip().split()))
    print("YES" if can_sort(p) else "NO")

def can_sort(p):
    for i in range(1, len(p)):
        if p[i-1] > p[i]:
            return True
    return False

if __name__ == '__main__':
    main()