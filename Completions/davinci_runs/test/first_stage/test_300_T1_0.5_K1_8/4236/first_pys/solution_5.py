

# SOLUTION
n, m = [int(i) for i in input().split()]

segments = []
for i in range(n):
    l, r = [int(i) for i in input().split()]
    segments.append([l, r])

segments.sort(key=lambda x: x[0])

# print(segments)

result = []
for i in range(m):
    for j in range(len(segments)):
        if i + 1 >= segments[j][0] and i + 1 <= segments[j][1]:
            break
        elif j == len(segments) - 1:
            result.append(i + 1)

print(len(result))
print(*result)