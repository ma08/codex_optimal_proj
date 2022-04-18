

import sys

r = int(sys.stdin.readline().rstrip()) # strip() 함수는 문자열의 양쪽의 공백을 제거한다.
g = int(sys.stdin.readline().rstrip())

print(int(g + (g-r)/2))
