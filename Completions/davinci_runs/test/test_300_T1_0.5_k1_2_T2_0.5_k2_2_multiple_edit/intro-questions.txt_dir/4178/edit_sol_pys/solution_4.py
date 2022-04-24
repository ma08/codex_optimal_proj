import sys

def main():
    n = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))
    if n == 1:
        print('Yes')
        return
    prev_h = 0
    for i in range(n):
        if i == 0:
            prev_h = heights[i]
        else:
            if heights[i] < prev_h:
                if heights[i] == 0:
                    print('No')
                    return
                heights[i] -= 1
            prev_h = heights[i]
        if i == n - 1:
            if heights[i] < prev_h:
                print('No')
                return
    print('Yes')


if __name__ == '__main__':
    main()
