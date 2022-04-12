
import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

for s in S:
    print(chr(ord(s) + N) if ord(s) + N <= ord('Z') else chr(ord(s) + N - ord('Z') + ord('A') - 1), end='') # end='' : print()의 기본 값은 \n이므로 개행을 없애기 위해서 추가

# ord() : character to ASCII code
# chr() : ASCII code to character
