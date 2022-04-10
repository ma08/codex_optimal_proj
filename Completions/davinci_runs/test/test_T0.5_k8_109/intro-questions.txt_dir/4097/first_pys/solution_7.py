

n = int(input())
b = list(map(int, input().split()))

def is_arithmetic(lst):
    if len(lst) <= 2:
        return True
    diff = lst[1] - lst[0]
    for i in range(1, len(lst) - 1):
        if lst[i + 1] - lst[i] != diff:
            return False
    return True

def get_min_changes(lst):
    if is_arithmetic(lst):
        return 0
    if len(lst) == 2:
        return -1
    if n == 3:
        return 1
    if lst[0] - lst[1] == lst[2] - lst[1]:
        return 1
    if lst[-1] - lst[-2] == lst[-3] - lst[-2]:
        return 1
    return 2

print(get_min_changes(b))