# https://codeforces.com/problemset/problem/1360/C


def main():
    n = int(input())
    for i in range(n):
        x = int(input())
        a = [int(i) for i in input().split()]
        a.sort()
        min_moves = 0
        for i in range(x):
            min_moves += abs(a[x-1] - a[i])
        print(min_moves)


if __name__ == '__main__':
    main()
