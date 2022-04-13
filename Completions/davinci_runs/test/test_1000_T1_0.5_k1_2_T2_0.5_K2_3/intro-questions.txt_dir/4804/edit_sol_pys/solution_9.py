
def find_patterns(n):
    patterns = []
    for x in range(1, n):
        y = n - x
        if x % 2 == 0 and y % 2 == 0 or x % 2 == 1 and y % 2 == 1:
            patterns.append([x, y])
        elif x % 2 == 1 and y % 2 == 1:
            patterns.append([x, y])
        elif x % 2 == 1 and y % 2 == 0:
            patterns.append([x, y])
        elif x % 2 == 0 and y % 2 == 1:
            patterns.append([x, y])
    return patterns

n = int(input())
patterns = find_patterns(n)
print(n, ':')
for x, y in patterns:
    print(x, y, sep=',')
