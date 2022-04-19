import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))
    if n == 1:
        print('Yes')
        return
    prev_h = heights[0]
    for i in range(1, n):
        curr_h = heights[i]
        if curr_h < prev_h:
            if curr_h == 0:
                print('No')
                return
            heights[i] -= 1
        prev_h = heights[i]
    print('Yes')
