n = int(input())
a = []
b = []


for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

a.sort()
b.sort()

if a == b:
    print("Poor Alex")
else: 
    print("Happy Alex")
