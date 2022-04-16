

import sys

def main():
    n, k = map(int, sys.stdin.readline().strip().split())
    if n < k:
        print("You will become a flying monkey!")
    else:
        print("Your wish is granted!")

if __name__ == '__main__':
    main()
