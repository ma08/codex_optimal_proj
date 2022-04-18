
import sys

a, b, c = map(int, sys.stdin.readline().split()) # 공백을 기준으로 입력받음

if a == 5 and b == 7 and c == 5: # 각 값이 5, 7, 5 이면 YES 출력
    print("YES")
else:
    print("NO")
