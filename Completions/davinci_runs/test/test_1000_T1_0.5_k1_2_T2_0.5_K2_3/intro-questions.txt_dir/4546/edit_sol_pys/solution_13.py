

import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().strip().split()) # 공백으로 구분된 숫자를 입력받아 int형으로 변환하여 a, b, c, d에 저장
    if b-a == c-b == d-c: # 등차수열의 정의에 따라 인접한 두 수의 차이가 같은지 확인
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
