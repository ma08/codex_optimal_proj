

n = int(input())
a = list(map(int, input().split()))

#print(n)
#print(a)

a.sort()

print(a)

#print(len(set(a)))

#print(a.count(a[0]))
#print(a.count(a[-1]))

#print(a.count(a[0])+a.count(a[-1]))

print(max(a.count(a[0]), a.count(a[-1])) + len(set(a)) - 1)