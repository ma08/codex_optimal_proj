

n, k = map(int, input().split())
s = input()

if k > n:
    print(-1)
else:
    print(n*k-sum(map(len, s.split(s[0]))))