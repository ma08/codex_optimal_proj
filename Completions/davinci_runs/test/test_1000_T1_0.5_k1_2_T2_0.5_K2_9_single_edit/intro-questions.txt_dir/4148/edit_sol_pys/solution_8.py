

import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()

for i in range(len(s)):
    if ord(s[i]) + n > ord("Z"):
        print(chr(ord(s[i]) + n - 26), end="")  # python3에서는 print문을 쓸 때 마지막에 end=""를 붙여주어야 줄바꿈이 되지 않습니다.
    else:
        print(chr(ord(s[i]) + n), end="")
