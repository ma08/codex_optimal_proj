
import sys
def read_ints():
    return [int(x) for x in sys.stdin.readline().strip().split()]


def main():
    t = int(input())
    for _ in range(t):
        n, k = read_ints()
        x = read_ints()
        y = read_ints()
        left = list(zip(x, y))
        right = list(zip(x, y))
        left = sorted(left)
        right = sorted(right)
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
