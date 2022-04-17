
import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) #split() 문자열을 공백을 기준으로 나누어 리스트로 반환

    if sheep < wolves:
        print("unsafe") # 값을 출력하기 위해서는 print() 함수를 사용
    else:
        print("safe")

if __name__ == '__main__': # 스크립트를 모듈로 사용하는 경우에는 if __name__ == '__main__' 이 부분이 실행되지 않음
    main()
