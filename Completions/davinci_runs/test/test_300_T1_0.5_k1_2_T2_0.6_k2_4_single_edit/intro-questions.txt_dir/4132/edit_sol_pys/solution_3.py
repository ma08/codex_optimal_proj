

n = int(input())
a = list(map(int, input().split()))

while len(a) > 1:
    a.remove(min(a))
    a.remove(max(a))
print(a[0])
