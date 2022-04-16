
n = int(input())
names = []
for _ in range(n):
    names.append(input())

if names == sorted(names):
    print("INCREASING"
elif names == sorted(names, reverse=True):
    print("DECREASING")
else:
    print("NEITHER")
