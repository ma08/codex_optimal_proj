
def get_groups(n, arr):
    groups = []
    for i in range(n):
        groups.append(arr[i])
    return groups

def get_sets(n, arr):
    sets = []
    for i in range(n):
        sets.append(set(arr[i]))
    return sets

def get_set_bounds(n, arr):
    bounds = []
    for i in range(n):
        bounds.append([arr[i][0], arr[i][-1]])
    return bounds

def find_groups(sets, set_bounds):
    bounds = get_set_bounds(len(sets), sets)
    while len(sets) > 1:
        i = 0
        j = 0
        while i < len(sets)-1:
            if i == len(sets)-1:
                break
            while j < len(sets):
                if j == len(sets):
                    break
                if sets[i] == sets[j]:
                    if bounds[i][1] + 1 == bounds[j][0] or bounds[j][1] + 1 == bounds[i][0]:
                        if bounds[i][0] < bounds[j][0]:
                            bounds[i][1] = bounds[j][1]
                        else:
                            bounds[i][0] = bounds[j][0]
                        bounds[j][0] = -1
                        bounds[j][1] = -1
                        sets.pop(j)
                        bounds.pop(j)
                        continue
                j += 1
            i += 1
            j = 0
    i = 0
    while i < len(bounds):
        if bounds[i][0] == -1:
            bounds.pop(i)
            continue
        i += 1
    i = 0
    while i < len(bounds):
        for j in range(len(set_bounds)):
            if set_bounds[j][0] <= bounds[i][0] and set_bounds[j][1] >= bounds[i][1]:
                bounds.pop(i)
                break
        i += 1
    return bounds

def main():
    n = int(input())
    arr = input().split()
    arr = [int(x) for x in arr]
    groups = get_groups(n, arr)
    sets = get_sets(n, groups)
    set_bounds = get_set_bounds(n, groups)
    groups = find_groups(sets, set_bounds)
    print(len(groups))
    for i in range(len(groups)):
        print(str(groups[i][0]) + " " + str(groups[i][1]))

if __name__ == "__main__":
    main()
