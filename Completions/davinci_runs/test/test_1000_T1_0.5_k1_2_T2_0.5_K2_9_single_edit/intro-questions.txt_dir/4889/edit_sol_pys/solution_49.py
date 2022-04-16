
n = int(input())

l = []
for i in range(n):
    l.append(int(input()))

l.sort(reverse = True)

output = 0
for i in range(n - 1):
    output += l.pop(0) - 1

output += l.pop(0)

print(output)
