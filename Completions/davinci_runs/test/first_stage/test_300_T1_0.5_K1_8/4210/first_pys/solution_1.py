
import sys
sys.setrecursionlimit(10000)

def main():
    n, k = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))

    def is_divisible(x, y):
        return int(str(x) + str(y)) % k == 0

    def count_divisible(i):
        total = 0
        for j in range(i):
            if is_divisible(a[i], a[j]):
                total += 1
        return total + count_divisible(i + 1) if i < n - 1 else 0

    print(count_divisible(0))


if __name__ == '__main__':
    main()