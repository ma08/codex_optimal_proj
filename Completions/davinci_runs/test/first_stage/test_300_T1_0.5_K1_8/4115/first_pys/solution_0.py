

import sys


def main():
    """
    メイン処理
    """
    s = sys.stdin.readline().rstrip()
    if s == s[::-1]:
        print(0)
    else:
        print(1)


if __name__ == '__main__':
    main()