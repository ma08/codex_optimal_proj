# https://www.acmicpc.net/problem/5525

import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()  # rstrip() : 오른쪽 공백 제거

for s in S:
    print(chr(ord(s) + N) if ord(s) + N <= ord('Z') else chr(ord(s) + N - ord('Z') + ord('A') - 1), end='')  # end='' : 개행 없음

# ord() : character to integer
# chr() : integer to character
