import sys

def main():
    n, x = map(int, sys.stdin.readline().split())
    x_list = [int(i) for i in sys.stdin.readline().split()]
    x_list.sort()

    if x in x_list:
        x_list.remove(x)

    min_d = max(x_list[0] - x, x - x_list[-1])
    for i in range(1, n):
        min_d = max(min_d, (x_list[i] - x_list[i - 1]) // 2)

    print(min_d)

if __name__ == '__main__':
    main()
