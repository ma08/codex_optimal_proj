# coding=utf-8

import sys

def main():
    cans = int(sys.stdin.readline())  # 读取第一行
    duras = [int(x) for x in sys.stdin.readline().split()]  # 读取第二行
    shot = 0
    shotList = []
    for i in range(cans):
        shotList.append(i+1)  # 排序用的列表
    shotList.sort(key=lambda x: duras[x-1])  # 按照duras列表中的元素排序
    for i in range(cans):
        shot += (duras[shotList[i]-1]*i+1)  # 加上每一次拍摄的时间
    print(shot)
    print(*shotList)  # 打印排序的结果

if __name__ == "__main__":
    main()
