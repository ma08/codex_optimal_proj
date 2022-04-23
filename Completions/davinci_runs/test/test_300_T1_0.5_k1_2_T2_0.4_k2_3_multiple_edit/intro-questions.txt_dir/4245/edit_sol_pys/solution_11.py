import sys

A, B = map(int, sys.stdin.readline().rstrip().split()) # 공백으로 구분된 정수들을 입력받음
print(B // A + (B % A != 0)) # B를 A로 나눈 몫과 나머지가 0이 아니면 1을 더한 값을 출력
