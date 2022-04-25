import sys

n, a, b = map(int, sys.stdin.readline().split())  # 공백으로 구분된 정수 3개 받기

print(min(n * a, b))  # n * a, b 중 작은 값 출력
