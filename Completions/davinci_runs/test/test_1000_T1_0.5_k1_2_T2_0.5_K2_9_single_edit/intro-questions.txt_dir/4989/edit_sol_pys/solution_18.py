
#Solution
n = int(raw_input())
a = [int(x) for x in raw_input().split()]
a.sort()

suma = sum(a[::2])
sumb = sum(a[1::2])

print(suma, sumb)
