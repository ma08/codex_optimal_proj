import sys

def main():
    n, x = map(int, input().split())
    x_lst = [int(i) for i in input().split()]
    x_lst = sorted(x_lst)

    min_d = max(x - x_lst[0], x_lst[-1] - x)

    for i in range(1, n):
        min_d = max(min_d, (x_lst[i] - x_lst[i-1]) // 2)

    print(min_d)

if __name__ == '__main__':
    main()
