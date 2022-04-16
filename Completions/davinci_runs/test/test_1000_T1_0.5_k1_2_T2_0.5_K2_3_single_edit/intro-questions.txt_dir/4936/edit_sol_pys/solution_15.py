

import sys

def main():
    n = int(sys.stdin.readline().strip())
    temp = [int(i) for i in sys.stdin.readline().strip().split()] # 字符串转数组
    max_temp = []
    for i in range(len(temp)-2):
        max_temp.append(max(temp[i], temp[i+1], temp[i+2])) # 找出每三个数中的最大值
    index = max_temp.index(min(max_temp)) # 找出最大值中的最小值
    print(index+1, max_temp[index]) # 打印最小最大值的位置

if __name__ == '__main__':
    main()
