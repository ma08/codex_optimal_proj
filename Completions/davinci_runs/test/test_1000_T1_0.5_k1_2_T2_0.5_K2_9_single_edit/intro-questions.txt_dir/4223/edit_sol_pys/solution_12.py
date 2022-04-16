

from itertools import combinations

n = int(input())  # the number of adjacency relations
data = []
for i in range(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(j) for j in input().split()]
    data.append((xi, yi))


def find_group(data):
    groups = []
    for d in data:
        # print(d)
        for g in groups:
            if d[0] in g or d[1] in g:
                g.add(d[0])
                g.add(d[1])
                break
        else:
            groups.append(set(d))
        # print(groups)
    return groups


def find_common(groups):
    common = set()
    for g in groups:
        for c in combinations(g, 2):
            common.add(c)
    return common


groups = find_group(data)
common = find_common(groups)


# print(groups)
# print(common)

# The minimal amount of steps required to completely propagate the advertisement
print(len(common))
