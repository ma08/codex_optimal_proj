

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())  # reads n and k from stdin
    if k < n:
        print("You will become a flying monkey!")  # print this if k < n
    else:
        print("Your wish is granted!")  # print this if k >= n

if __name__ == '__main__':
    main()
