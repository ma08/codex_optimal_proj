

import sys # 파일 입출력 패키지

N = int(sys.stdin.readline().rstrip()) # 입력받은 줄의 마지막 공백 제거
A = list(map(int, sys.stdin.readline().rstrip().split())) # 공백을 기준으로 리스트 생성, 리스트 요소들을 int로 변환

A.sort() # 리스트 정렬

print(A[N-1] - A[0]) # 리스트의 마지막 요소와 첫번째 요소의 차이 출력
