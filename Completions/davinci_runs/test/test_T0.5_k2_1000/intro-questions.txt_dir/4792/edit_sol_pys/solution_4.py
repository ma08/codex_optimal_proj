

def remove_adjacent(lst):
    i = 0

    while i < len(lst) - 1:
        if lst[i] == lst[i + 1]:
            lst = lst[:i + 1] + lst[i + 2:]
        else:
            i += 1

    return lst
