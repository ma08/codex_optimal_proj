

n = int(input())
a = list(map(int, input().split()))


def get_max_index(arr):
    max_v = max(arr)
    for i, v in enumerate(arr):
        if v == max_v:
            return i


def get_min_index(arr):
    min_v = min(arr)
    for i, v in enumerate(arr):
        if v == min_v:
            return i


a[get_max_index(a)] = -1
a[get_min_index(a)] = -1

print(max(a))
