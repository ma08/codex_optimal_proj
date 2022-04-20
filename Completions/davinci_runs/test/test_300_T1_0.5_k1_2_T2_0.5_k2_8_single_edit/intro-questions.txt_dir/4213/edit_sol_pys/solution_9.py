

import sys

N = int(sys.stdin.readline().rstrip()) # 입력받은 숫자를 정수로 변환
A = list(map(int, sys.stdin.readline().rstrip().split())) # 입력받은 문자열을 정수로 변환하며, 리스트로 저장

A.sort() # 정렬

print(A[N-1] - A[0]) # 정렬된 리스트의 첫번째 값과 마지막 값의 차이를 출력
