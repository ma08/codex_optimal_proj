
import sys


def main():
    # input
    a, b, c = map(int, sys.stdin.readline().rstrip().split())  # readline()で改行を含めて読み込む

    # main
    ans = min(b // a, c)  # 商を出す時は//を使う

    # output
    print(ans)


if __name__ == '__main__':
    main()
