import sys
sys.setrecursionlimit(10 ** 7)
n,m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
bc = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]


bc = sorted(bc,key=lambda x:x[1],reverse=True)

ans = 0

i = 0

while i<m and a:
    b = bc[i][0]
    c = bc[i][1]

    j = 0

    while j<b and a:
        ans += c
        a.pop()
        j += 1

    i += 1

print(ans+sum(a))
