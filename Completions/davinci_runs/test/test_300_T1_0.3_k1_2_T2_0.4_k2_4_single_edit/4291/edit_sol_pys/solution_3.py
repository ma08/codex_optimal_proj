
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()
b.sort()
print(a)
print(b)
for i in range(m):
    print(a[i])
