
import sys

def main():
    k = int(sys.stdin.readline().strip())  # 获取k的值
    i = 1
    while True:  # 循环，直到找到第一个最小的整数n
        if not (7 * (10 ** i) - 7) % k:  # 判断7 * 10 ^ n - 7是否能被k整除
            print(i + 1)  # 输出n的值
            break  # 终止循环
        i += 1  # 循环变量+1


if __name__ == '__main__':
    main()
