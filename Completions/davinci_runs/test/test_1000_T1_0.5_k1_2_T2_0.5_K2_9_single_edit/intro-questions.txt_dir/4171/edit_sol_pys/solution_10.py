n = int(input())
a, b = map(int, input().split())
k = int(input())
p = list(map(int, input().split()))
p.append(a)
p.append(b)
if len(set(p)) == k + 2:
    print('YES')
else: print('NO')
