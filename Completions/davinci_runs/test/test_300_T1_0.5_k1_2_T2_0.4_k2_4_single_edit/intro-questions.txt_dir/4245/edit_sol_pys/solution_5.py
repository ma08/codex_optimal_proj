
import sys

A, B = map(int, sys.stdin.readline().rstrip().split()) # A와 B를 입력받고, 두 수를 나눈 몫과 나머지를 구한다.
print(B // A + (B % A != 0)) # 몫과 나머지를 구한 후, 몫에 1을 더하고, 나머지가 0이 아니면 1을 더한다.
