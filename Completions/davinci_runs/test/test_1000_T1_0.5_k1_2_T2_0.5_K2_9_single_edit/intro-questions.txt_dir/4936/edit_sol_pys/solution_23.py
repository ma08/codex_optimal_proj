# -*- coding: utf-8 -*-

import sys

def main():
    n = int(sys.stdin.readline().strip())
    temp = [int(i) for i in sys.stdin.readline().strip().split()] # 读取一行的数据并转换为整数
    max_temp = []
    for i in range(len(temp)-2):
        max_temp.append(max(temp[i], temp[i+1], temp[i+2]))
    index = max_temp.index(min(max_temp))
    print(index+1, max_temp[index]) # 输出结果

if __name__ == '__main__':
    main()
