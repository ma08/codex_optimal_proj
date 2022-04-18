

import sys

def main():
    N, K = map(int, sys.stdin.readline().strip().split())
    print("Your wish is granted!" if K >= N else "You will become a flying monkey!")

if __name__ == '__main__':
    main()
