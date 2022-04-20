

s = input().split()

for i in s:
    if i == i[::-1]:
        print(0)
    else:
        print(1)
