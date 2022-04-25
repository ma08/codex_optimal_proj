


import sys

def main():
    x, k, d = map(int, sys.stdin.readline().rstrip().split())
    if abs(x) < k * d:  # xがk*dより小さい場合
        print(abs(x - (x // d) * d))  # 小数点以下を切り捨てて、その差を求める
    else:
        print(abs(x) - (k * d))  # xがk*dより大きい場合は、その差を求める

if __name__ == '__main__':
    main()
