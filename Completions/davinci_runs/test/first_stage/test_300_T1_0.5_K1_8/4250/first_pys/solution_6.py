

def find_max_indices(l, max_size):
    l_size = len(l)
    indices = []
    for i in range(l_size):
        if len(indices) < max_size:
            indices.append(i)
        else:
            min_index = min(indices)
            if l[i] > l[min_index]:
                indices.remove(min_index)
                indices.append(i)
    return indices


def find_max_indices_dict(l, max_size):
    l_size = len(l)
    indices = {}
    for i in range(l_size):
        if len(indices) < max_size:
            indices[i] = l[i]
        else:
            min_index = min(indices, key=indices.get)
            if l[i] > indices[min_index]:
                del indices[min_index]
                indices[i] = l[i]
    return indices


def find_max_indices_dict_sorted(l, max_size):
    l_size = len(l)
    indices = {}
    for i in range(l_size):
        if len(indices) < max_size:
            indices[i] = l[i]
        else:
            for j in sorted(indices, key=indices.get):
                if l[i] > indices[j]:
                    del indices[j]
                    indices[i] = l[i]
                    break
    return indices


def find_max_indices_dict_sorted_bisect(l, max_size):
    l_size = len(l)
    indices = {}
    for i in range(l_size):
        if len(indices) < max_size:
            indices[i] = l[i]
        else:
            for j in sorted(indices, key=indices.get):
                if l[i] > indices[j]:
                    del indices[j]
                    indices[i] = l[i]
                    break
    return indices


def find_max_indices_dict_sorted_bisect_bis(l, max_size):
    l_size = len(l)
    indices = {}
    for i in range(l_size):
        if len(indices) < max_size:
            indices[i] = l[i]
        else:
            for j in sorted(indices, key=indices.get):
                if l[i] > indices[j]:
                    del indices[j]
                    indices[i] = l[i]
                    break
    return indices

if __name__ == "__main__":
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    s_count = Counter(s)
    s_max = max(s_count.values())
    s_max_indices = find_max_indices(s_count.values(), k)
    s_max_indices_dict = find_max_indices_dict(s_count.values(), k)
    s_max_indices_dict_sorted = find_max_indices_dict_sorted(s_count.values(), k)
    s_max_indices_dict_sorted_bisect = find_max_indices_dict_sorted_bisect(s_count.values(), k)
    s_max_indices_dict_sorted_bisect_bis = find_max_indices_dict_sorted_bisect_bis(s_count.values(), k)
    print(s_max_indices_dict_sorted_bisect_bis)