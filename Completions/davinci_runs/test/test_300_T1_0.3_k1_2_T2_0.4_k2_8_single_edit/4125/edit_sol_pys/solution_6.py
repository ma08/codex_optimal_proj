import sys

def main():
    n, x = map(int, sys.stdin.readline().split())
    x_lst = [int(i) for i in sys.stdin.readline().split()]
    x_lst.sort()

    if x in x_lst:
        x_lst.remove(x)

    min_d = max(x_lst[0] - x, x - x_lst[-1])
    for i in range(1, n):
        min_d = max(min_d, (x_lst[i] - x_lst[i - 1]) // 2)

    print(min_d)

if __name__ == '__main__':
    main()
