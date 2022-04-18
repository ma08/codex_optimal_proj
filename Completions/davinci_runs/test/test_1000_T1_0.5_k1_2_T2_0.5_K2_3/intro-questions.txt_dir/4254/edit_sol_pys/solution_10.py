

import sys

def main():
    sheeps, wolfs = map(int, sys.stdin.readline().split())
    if sheeps < wolfs:
        print("unsafe")
    else:
        print("safe")
if __name__ == '__main__':
    main()
