

def get_groups(n, arr):
    groups = []
    i = 0
    while i < n:
        groups.append([arr[i], arr[i+1]])
        i += 2
    return groups

def get_sets(n, arr):
    sets = []
    i = 0
    while i < n:
        sets.append(set(range(arr[i][0], arr[i][1] + 1)))
        i += 1
    return sets

def get_set_bounds(n, arr):
    bounds = []
    i = 0
    while i < n:
        bounds.append([arr[i][0], arr[i][1]])
        i += 1
    return bounds

def get_bounds(n, arr):
    bounds = []
    i = 0
    while i < n:
        bounds.append([arr[i][0], arr[i][1]])
        i += 1
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
                if j == len(sets) - 1:
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
    return bounds

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
