

import sys

def main():
    n = int(input()) # 整数の入力
    a = list(map(int, input().split())) # スペース区切りの整数の入力
    a.sort()
    print(a[-1] - a[0])

if __name__ == '__main__':
    main()
