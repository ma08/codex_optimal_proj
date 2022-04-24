import sys

n = int(input())
list = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    list.append((a, b))

list.sort(key=lambda x: x[1])

end = 0
for i in range(n):
    if end <= list[i][0]:
        end = list[i][1]
    else:
        print(0)
        exit()
print(1)
