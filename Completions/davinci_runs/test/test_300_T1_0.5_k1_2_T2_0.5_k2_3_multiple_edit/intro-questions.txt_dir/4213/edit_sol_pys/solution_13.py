
# 입력으로 주어진 N개의 정수 중에서 가장 큰 수와 가장 작은 수의 차이를 출력하는 프로그램을 작성하시오
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

A.sort()

print(A[N-1] - A[0])
