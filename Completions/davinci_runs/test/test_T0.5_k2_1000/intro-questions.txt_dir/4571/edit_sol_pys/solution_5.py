
from sys import stdin

def main():
    n, m = map(int, stdin.readline().split())  # n: 年数, m: 分岐回数
    if m == 0:
        print(n * 100)  # 分岐回数が0回の場合
    elif m == 1:
        print(n * 100 + 1900)  # 分岐回数が1回の場合
    else:
        print(n * 100 + 1900 * sum([(1 / 2) ** i for i in range(1, m)]))

if __name__ == '__main__':
    main()
