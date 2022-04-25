import sys


def main():
    n = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))
    if n == 1:
        print('Yes')
        return
    prev_h = heights[0]
    for i in range(1, n):
        curr_h = heights[i]
        if curr_h < prev_h and curr_h == 0:
            print('No')
            return
        if curr_h < prev_h: 
            heights[i] -= 1
        prev_h = heights[i]
    print('Yes')


if __name__ == '__main__':
    main()
