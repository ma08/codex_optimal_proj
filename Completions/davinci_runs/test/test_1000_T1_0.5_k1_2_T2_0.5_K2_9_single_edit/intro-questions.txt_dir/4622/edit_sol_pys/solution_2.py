import sys

n = int(sys.stdin.readline())
a = list(map(int, input().split()))

def check_repeat(n, a):
    if len(set(a)) == n:
        print("YES")
    else:
        print("NO")

check_repeat(n, a)
