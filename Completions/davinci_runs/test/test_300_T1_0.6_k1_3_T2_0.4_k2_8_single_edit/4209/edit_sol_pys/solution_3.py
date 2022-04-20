


def get_groups(arr):
    groups = [[arr[0]]]
    i = 0
    j = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            groups[j].append(arr[i+1])
        else:
            groups.append([arr[i+1]])
            j += 1
        i += 1
    return groups


def get_sets(arr):
    sets = [set(arr[0])]
    i = 0
    j = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            sets[j].add(arr[i+1])
        else:
            sets.append(set(arr[i+1]))
            j += 1
        i += 1
    return sets


def get_set_bounds(arr):
    bounds = []
    for i in range(len(arr)):
        bounds.append([min(arr[i]), max(arr[i])])
    return bounds


def get_bounds(arr):
    bounds = []
    for i in range(len(arr)):
        bounds.append([arr[i][0], arr[i][-1]])
    return bounds


def find_groups(arr):
    groups = get_groups(arr)
    sets = get_sets(groups)
    bounds = get_bounds(groups)
    set_bounds = get_set_bounds(groups)
    while len(sets) > 1:
        i = 0
        j = 0
        while i < len(sets) - 1:
            if i == len(sets) - 1:
                break
            while j < len(sets):
                if j == len(sets):
                    break
                if sets[i] == sets[j]:
                    if bounds[i][1] + 1 == bounds[j][0] or \
                            bounds[j][1] + 1 == bounds[i][0]:
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
            if set_bounds[j][0] == bounds[i][0] and set_bounds[j][1] == bounds[i][1]:
                set_bounds.pop(j)
        i += 1
    i = 0
    while i < len(set_bounds):
        if set_bounds[i][0] == -1:
            set_bounds.pop(i)
            continue
        i += 1
    return bounds + set_bounds


def main():
    n = int(input())
    arr = input().split()
    arr = [int(x) for x in arr]
    groups = find_groups(arr)
    print(len(groups))
    for i in range(len(groups)):
        print(str(groups[i][0]) + " " + str(groups[i][1]))


if __name__ == "__main__":
    main()
