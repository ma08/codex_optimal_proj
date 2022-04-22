

import sys

def main():
    n = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().strip())) # 문자열로 인식
    f = list(map(int, sys.stdin.readline().strip().split())) # 공백으로 구분해서 리스트로 인식
    for i in range(len(num)):
        num[i] = f[num[i]] # f에서 num에 있는 수를 가지고 온다.
    print(''.join(map(str, num))) # 리스트 -> 문자열


if __name__ == '__main__':
    main()
