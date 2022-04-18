#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline().strip())  # 学生的数量
    recite = [int(sys.stdin.readline().strip()) for _ in range(n)]  # 已经背诵的诗的编号
    missing = []
    for i in range(1, recite[-1] + 1):  # 诗的编号是从1开始, 需要背诵到最后一首诗的编号
        if i not in recite:  # 没有背诵的诗
            missing.append(i)  # 记录下来
    if len(missing) > 0:
        for m in missing:
            print(m)
    else:
        print("good job")

if __name__ == "__main__":
    main()
