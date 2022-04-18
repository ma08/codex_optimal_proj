

import sys

def main():
    S, C, K = [int(i) for i in sys.stdin.readline().split()]
    Socks = [int(i) for i in sys.stdin.readline().split()]
    Socks.sort()
    i = 0
    count = 0
    while i < S:
        count += 1
        j = i + 1
        while j < S and Socks[j] - Socks[i] <= K:
            j += 1
        i = j
    print(count)

if __name__ == '__main__':
    main()
