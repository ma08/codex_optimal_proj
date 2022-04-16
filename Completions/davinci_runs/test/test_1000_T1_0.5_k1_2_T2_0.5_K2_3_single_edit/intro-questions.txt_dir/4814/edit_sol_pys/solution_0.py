
num = int(input())
names = []

for i in range(num):
    names.append(input())

if names == sorted(names, key=str.lower):
    print("INCREASING")
elif names == sorted(names, reverse=True, key=str.lower):
    print("DECREASING")
else:
    print("NEITHER")
