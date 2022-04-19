

import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split()) # a,b,c,d 입력받기
    count = 0 # 카운트 변수 초기화

    for i in range(a, b+1):
        if i % c != 0 and i % d != 0: # c,d로 나눈 나머지가 0이 아니면 카운트 증가
            count += 1 

    print(count) # 카운트 출력

if __name__ == '__main__':
    main()
