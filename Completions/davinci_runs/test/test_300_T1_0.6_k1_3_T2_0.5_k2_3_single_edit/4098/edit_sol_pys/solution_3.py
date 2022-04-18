
n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
for i in range(m):
    a[i] += 1
    a[i+1] += 1
    if a[i] % 2 == 0:
        print(i+1)
        break
else:
    print(n)
# print(a)
