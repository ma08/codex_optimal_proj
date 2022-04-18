t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    for _ in range(m):
        a, b = map(int, input().split())
        print(s[a:b])
