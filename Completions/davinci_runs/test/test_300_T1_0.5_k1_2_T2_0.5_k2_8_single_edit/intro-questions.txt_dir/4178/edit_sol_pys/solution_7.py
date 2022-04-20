import sys
sys.setrecursionlimit(10**6)


def main():
    n = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))

    for i in range(1, n):
        if heights[i - 1] > heights[i]:
            heights[i] += 1

    for i in range(1, n):
        if heights[i - 1] > heights[i]:
            sys.stdout.write('No')
            break
    else:
        sys.stdout.write('Yes')


if __name__ == '__main__':
    main()
