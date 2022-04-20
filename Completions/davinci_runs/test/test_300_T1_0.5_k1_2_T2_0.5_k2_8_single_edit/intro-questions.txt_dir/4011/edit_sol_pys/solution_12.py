

import sys

def main():
    n = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().strip())) # 这里是读取数字，直接转变成整型不行，需要先转换成str，然后再转换成int
    f = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(len(num)):
        num[i] = f[num[i]-1] # 因为是从1开始的所以要减1
    print(''.join(map(str, num)))


if __name__ == '__main__':
    main()
