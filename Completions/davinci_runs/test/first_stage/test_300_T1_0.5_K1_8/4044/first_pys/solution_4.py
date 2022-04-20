

a, b, x = map(int, input().split())

s = ""
for i in range(x):
    s += "01"
for i in range(a - x):
    s += "0"
for i in range(b - x):
    s += "1"

print(s)