import sys
import math
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split())) # 입력 받은 값을 리스트로 변환
a.sort(reverse=True) # 큰 값부터 정렬
b = [] # 정렬된 값을 저장할 리스트

for i in range(n):
    b.append(a.pop(0)) # 가장 큰 값을 리스트 b에 저장
    if a and a[0]*2 == b[-1]: # a 리스트에 값이 있고, a 리스트의 첫번째 값이 b 리스트의 마지막 값의 2배일 때
        b.append(a.pop(0)) # a 리스트의 첫번째 값을 b 리스트에 저장
print(' '.join(map(str, b))) # b 리스트 출력
