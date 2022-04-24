import sys
input = sys.stdin.readline

S = input()
T = input()

if S == T[:-1]:
    print('Yes')
else:
    print('No')
