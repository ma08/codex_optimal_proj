n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))


ans = sum(b)

for i in range(len(a)):
    if i != 0 and a[i] == a[i - 1] + 1:
        ans += c[a[i - 1] - 1]

print(ans)
