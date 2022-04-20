

import sys

def main():
    rp = list(map(int, sys.stdin.readline().split()))
    print(min([rp[i] - rp[i - 1] for i in range(1, len(rp))]))

if __name__ == '__main__':
    main()