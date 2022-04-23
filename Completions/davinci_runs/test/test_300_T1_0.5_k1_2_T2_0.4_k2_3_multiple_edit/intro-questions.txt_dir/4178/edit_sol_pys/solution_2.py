import sys


def main():
    n = int(input())
    heights = list(map(int, input().split()))
    if n == 1:
        print('YES')
        return
    prev_h = heights[0]
    for i in range(1, n):
        curr_h = heights[i]
        if curr_h < prev_h:
            if curr_h == 0:
                print('NO')
                return
            heights[i] -= 1
        prev_h = heights[i]
    print('YES')


if __name__ == '__main__':
    main()
