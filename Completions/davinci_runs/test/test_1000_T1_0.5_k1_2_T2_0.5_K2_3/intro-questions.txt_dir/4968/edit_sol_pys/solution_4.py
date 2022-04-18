

n, s, r = map(int, input().split()) 
d = set(map(int, input().split())) 
b = set(map(int, input().split()))

c = 0

for i in range(1, n+1):
    if i in d:
        if i-1 in b:
            b.remove(i-1)
        elif i+1 in b:
            b.remove(i+1)
        else:
            c += 1
print(c)
