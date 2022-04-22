import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


s = input()
t = input().rstrip()

ans = 0
for i in range(len(s)):
    if s[i] != t[i]:
        ans += 1

print(ans, end="\n")
