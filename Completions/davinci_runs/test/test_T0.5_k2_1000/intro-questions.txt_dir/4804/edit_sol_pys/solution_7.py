

def find_patterns(n):
    patterns_list = []
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if x + y == n:
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
patterns_list = find_patterns(n)
print(n, ':')
for x, y in patterns_list:
    print(x, y, sep=',')
