import sys

N = int(input())
sequence = list(map(int, sys.stdin.readline().split()))

if(sequence == sorted(sequence)):
    print("YES")
else:
    print("NO")
