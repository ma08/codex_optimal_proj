

import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())  # a, b, c, d를 입력받아서 정수형으로 변환한 후 변수에 할당
    count = 0

    for i in range(a, b+1):  # a부터 b까지 반복
        if i % c != 0 and i % d != 0:  # i가 c와 d의 배수가 아니라면
            count += 1  # count에 1을 더한다

    print(count)  # count를 출력한다

if __name__ == '__main__':
    main()
