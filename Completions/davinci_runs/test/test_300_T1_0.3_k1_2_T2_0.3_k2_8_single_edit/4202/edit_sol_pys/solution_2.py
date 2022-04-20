
import sys

def main():
    l, r = map(int, sys.stdin.readline().split())  # 区間
    mod = 2019
    min_mod = mod
    for i in range(l, r):  # 区間の最初から最後まで
        for j in range(i+1, r+1):  # 区間の最初+1から最後まで
            min_mod = min(min_mod, (i*j)%mod)  # 一番小さいmodを求める
    print(min_mod)

if __name__ == '__main__':
    main()
