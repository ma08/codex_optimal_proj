

import sys

def main():
    H, W = map(int, sys.stdin.readline().rstrip().split())
    h, w = map(int, sys.stdin.readline().rstrip().split())
    print(H*W - (h*W + w*H - h*w))

if __name__ == '__main__':
    main()