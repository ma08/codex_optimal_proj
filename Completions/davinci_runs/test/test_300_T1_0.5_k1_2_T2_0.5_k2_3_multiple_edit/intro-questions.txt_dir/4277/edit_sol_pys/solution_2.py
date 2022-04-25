
import sys

n, a, b = map(int, sys.stdin.readline().split()) # n, a, b를 int형으로 입력받아서 저장

print(min(n*a, b)) # n*a와 b 중 작은 값을 출력
