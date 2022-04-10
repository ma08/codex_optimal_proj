# https://codeforces.com/problemset/problem/1360/B


def main():
    n = int(input())
    for i in range(n):
        x = [int(i) for i in input().split()]
        x.sort()
        if n%2 == 0:
            mid = n//2
        else:
            mid = n//2 + 1
        min_moves = 0
        for i in range(n):
            min_moves += abs(x[mid-1] - x[i])
        print(min_moves)


if __name__ == '__main__':
    main()
