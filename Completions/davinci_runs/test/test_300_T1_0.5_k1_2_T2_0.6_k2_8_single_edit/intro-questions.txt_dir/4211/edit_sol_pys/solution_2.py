
def read_ints():
    return list(map(int, input().split())


n = int(input())
b = read_ints()

ans = 0

for i in range(n):
    ans += min(b[i], b[i+1])

a.append(b[n-2])

print(sum(a))
