import sys


def solve(n, heights):
    prev_h = heights[0]
    for i in range(1, n):
        curr_h = heights[i]
        if curr_h < prev_h:
            if curr_h == 0:
                return False
            heights[i] -= 1
        prev_h = heights[i]
    return True


def main():
    n = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))
    if n == 1:
        print('Yes')
        return
    if solve(n, heights):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
