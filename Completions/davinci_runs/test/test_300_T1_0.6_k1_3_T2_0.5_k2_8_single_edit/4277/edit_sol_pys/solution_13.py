

import sys
import math

def main():
    nums = sys.stdin.readline().rstrip().split()
    N = int(nums[0]) # 行
    A = int(nums[1]) # 1行当たりの料金
    B = int(nums[2]) # 最大料金
    print(min(N*A, B)) # 行 * 1行当たりの料金 と 最大料金 のうち小さい方を出力

if __name__ == '__main__':
    main()
