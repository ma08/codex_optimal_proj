import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


n, k = map(int, input().split())
s = readline().rstrip().decode('utf-8')

ans = 0

for i in range(n):
    if s[i] == '1':
        continue
    if i - k >= 0 and s[i - k] == '1':
        continue
    if i + k < n and s[i + k] == '1':
        continue
    ans += i + 1

print(ans)
