

import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split())  # 使用map函数将输入的字符串转换为数字
    if sheep < wolves:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
