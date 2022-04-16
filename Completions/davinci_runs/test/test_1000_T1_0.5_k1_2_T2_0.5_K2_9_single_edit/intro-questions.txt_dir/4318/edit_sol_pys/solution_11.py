

import sys

def main():
    n = int(sys.stdin.readline())
    h = list(map(int, sys.stdin.readline().split())
    count = 0
    for i in range(n):
        if h[i] >= max(h[:i+1]):
            count += 1
    print(count

if __name__ == "__main__":
    main()
