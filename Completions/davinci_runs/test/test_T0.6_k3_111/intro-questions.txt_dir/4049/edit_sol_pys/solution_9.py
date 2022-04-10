

# Solved by Shashwat Raj

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

r = a[2] + b[1]
p = a[1] + b[2]
s = a[0] + b[0]

print(min(r, min(p, s)), max(r, max(p, s)))
