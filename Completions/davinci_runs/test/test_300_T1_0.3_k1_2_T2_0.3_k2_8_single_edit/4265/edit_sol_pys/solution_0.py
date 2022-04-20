import sys
input = sys.stdin.readline


s = input().rstrip()
t = input().rstrip()

count = 0

for i in range(len(s)):
    if s[i] != t[i]:
        count += 1

print(count)
