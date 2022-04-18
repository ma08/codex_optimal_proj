

import os
import sys

def main():
    print(sys.argv)

    if len(sys.argv) == 1:
        print("引数が足りません")
        sys.exit(1)

    # 引数の数を取得
    argc = len(sys.argv)
    # 引数を順番に取得
    for i in range(1, argc):
        print(sys.argv[i])

if __name__ == '__main__':
    main()
