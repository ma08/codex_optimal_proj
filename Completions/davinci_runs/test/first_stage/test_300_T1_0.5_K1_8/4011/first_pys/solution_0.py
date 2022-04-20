

#Solution

n = int(input())
a = list(input())
f = list(map(int, input().split()))
for i in range(n):
    a[i] = str(f[int(a[i])-1])
print(''.join(a))