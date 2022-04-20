

def get_groups(n, arr):
    groups = []
    for i in range(n):
        groups.append([arr[i]])
    return groups

def get_sets(n, arr):
    sets = []
    for i in arr:
        sets.append(set(i))
    return sets

def get_set_bounds(n, arr):
    bounds = []
    for i in arr:
        bounds.append([i[0], i[0]])
    return bounds

def get_bounds(n, arr):
    bounds = []
    for i in arr:
        bounds.append([i[0], i[0]])
    return bounds

def find_groups(n, arr):
    groups = get_groups(n, arr)
    sets = get_sets(n, groups)
    bounds = get_bounds(n, groups)
    set_bounds = get_set_bounds(n, groups)
    while len(sets) > 0:
        i = 0
        j = 0
        while i < len(sets):
            if i == len(sets):
                break
            while j < len(sets):
                if j == len(sets):
                    break
                if sets[i] == sets[j]:
                    if bounds[i][1] + 1 == bounds[j][0]:
                        bounds[i][1] = bounds[j][1]
                        bounds.pop(j)
                        sets.pop(j)
                        continue
                    elif bounds[j][1] + 1 == bounds[i][0]:
                        bounds[i][0] = bounds[j][0]
                        bounds.pop(j)
                        sets.pop(j)
                        continue
                j += 1
            i += 1
            j = 0
    i = 0
    while i < len(set_bounds):
        for j in range(len(bounds)):
            if set_bounds[i][0] == bounds[j][0] and set_bounds[i][1] == bounds[j][1]:
                set_bounds.pop(i)
                continue
        i += 1
    i = 0
    while i < len(bounds):
        if bounds[i][0] == -1:
            bounds.pop(i)
            continue
        i += 1
    i = 0
    while i < len(bounds):
        if bounds[i][0] == -1:
            bounds.pop(i)
            continue
        i += 1
    return bounds + set_bounds

def main():
    n = int(input())
    arr = input().split()
    arr = [int(x) for x in arr]
    groups = find_groups(n, arr)
    print(len(groups))
    for i in range(len(groups)):
        print(str(groups[i][0]) + " " + str(groups[i][1]))

if __name__ == "__main__":
    main()
