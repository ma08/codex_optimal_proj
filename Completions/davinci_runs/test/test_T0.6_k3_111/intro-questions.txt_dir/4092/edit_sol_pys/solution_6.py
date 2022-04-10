
n = int(input())  # input size of array
a = list(map(int, input().split()))  # input array

neg = []  # list for negative numbers
pos = []  # list for positive numbers

for i in a:
    if i < 0:
        neg.append(i)
    elif i > 0:
        pos.append(i)
    else:
        pass

cnt = 0

if len(neg) % 2 == 0:
    cnt = 0
else:
    cnt = 1

print(cnt + len(pos) + len(neg))
