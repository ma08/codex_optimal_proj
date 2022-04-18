
import sys

def read_ints(n):
    return [int(x) for x in sys.stdin.readline().strip().split()[:n]]


def main():
    t = int(input())
    for _ in range(t):
        n, k = read_ints(2)
        x = read_ints(n)
        y = read_ints(n)
        points = list(zip(x, y))
        points.sort()
        left = [y for x, y in points]
        right = [y for x, y in points]
        left.sort()
        right.sort()
        i = 0
        j = 0
        ans = 0
        while i < n and j < n:
            if left[i] <= right[j]:
                i += 1
                ans += 1
            else:
                j += 1
        print(ans)


if __name__ == '__main__':
    main()
