import sys

A, B = map(int, sys.stdin.readline().rstrip().split())  # 공백으로 구분해서 입력받기
print(B // A + (B % A != 0))  # 소수점 아래는 버리고 정수만 구하기
