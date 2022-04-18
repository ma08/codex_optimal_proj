

num = int(input("Enter the number of names: "))
names = []

for i in range(num):
    names.append(input("Enter name: "))

if names == sorted(names):
    print("INCREASING")
elif names == sorted(names, reverse=True):
    print("DECREASING")
else:
    print("NEITHER")
