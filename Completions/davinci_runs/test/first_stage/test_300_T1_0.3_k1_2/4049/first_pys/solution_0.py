

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    print(max(0, min(a[2], b[0]) - max(a[0], b[2])), max(0, min(a[2], b[0]) - max(a[0], b[2])) + min(a[2], b[2]))

if __name__ == "__main__":
    main()