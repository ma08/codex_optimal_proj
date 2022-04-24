
import sys
sys.stdin = open("input.txt", "r")

d, t, s = map(int, input().split())

if d/t <= s:
    print('Yes')
else:
    print('No')
