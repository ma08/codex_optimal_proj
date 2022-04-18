

import math

def main():
    # input
    W, H, x, y = map(int, input().split())
    # compute
    if x == 0 or x == W or y == 0 or y == H or (x == W/2 and y == H/2):
        print(W*H/2, 1)
    else:
        print(W*H/2, 0)

if __name__ == '__main__':
    main()
