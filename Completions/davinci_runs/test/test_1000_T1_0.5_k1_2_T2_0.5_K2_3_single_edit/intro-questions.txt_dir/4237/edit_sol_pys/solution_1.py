

import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())  # a, b, c, d를 입력받음
    count = 0

    for i in range(a, b+1):  # a부터 b까지 반복
        if i % c != 0 and i % d != 0:  # i가 c와 d의 배수가 아니라면
            count += 1  # count를 1 증가

    print(count)

if __name__ == '__main__':
    main()
