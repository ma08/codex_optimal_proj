import sys

N = int(sys.stdin.readline().rstrip())  # 입력받은 문자열의 공백을 제거한 후 정수로 변환
A = list(map(int, sys.stdin.readline().rstrip().split()))  # map(function, iterable, ...) -> 입력받은 문자열을 공백을 기준으로 분리한 후, 각각의 문자열을 int형으로 변환하여 리스트로 저장

A.sort()

print(A[N-1] - A[0])
