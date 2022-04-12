
def find_patterns(n):
    patterns_list = []
    for x in range(1, n):
        y = n - x
        if x > y:
            break
        if x % 2 == 0 and y % 2 == 0:
            patterns_list.append([x, y])
        elif x % 2 == 1 and y % 2 == 1:
            patterns_list.append([x, y])
        elif x % 2 == 1 and y % 2 == 0:
            patterns_list.append([x, y])
        elif x % 2 == 0 and y % 2 == 1:
            patterns_list.append([x, y])
    return patterns_list

n = int(input())
patterns = find_patterns(n)
print(n, ':')
for x, y in patterns:
    print(x, y, sep=',')
