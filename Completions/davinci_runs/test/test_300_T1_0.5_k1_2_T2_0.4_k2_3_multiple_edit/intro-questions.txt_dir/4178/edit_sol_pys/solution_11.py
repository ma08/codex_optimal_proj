import sys

def main():
    n = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))
    if n == 1:
        print('Yes')
        return
    prev_height = heights[0]
    for i in range(1, n):
        curr_height = heights[i]
        if curr_height < prev_height:
            if curr_height == 0:
                print('No')
                return
            heights[i] -= 1
        prev_height = heights[i]
    print('Yes')


if __name__ == '__main__':
    main()
