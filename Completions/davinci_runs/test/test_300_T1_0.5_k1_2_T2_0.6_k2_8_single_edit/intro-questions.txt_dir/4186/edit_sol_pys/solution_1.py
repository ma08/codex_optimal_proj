

n = int(input())
a = list(map(int, input().split()))

s = set()
for i in a:
    s.add(i)

ans = 0
for i in s:
    ans += n - 2

print(ans)
