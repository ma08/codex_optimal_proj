

def find_min_arr(a, b):
    if a == b:
        return 1, 1
    if a < b:
        a, b = b, a
    if a % 2 == 0 and b % 2 == 0:
        return a // 2, b
    elif a % 2 == 0 and b % 2 == 1:
        return find_min_arr(a // 2, b)
    elif a % 2 == 1 and b % 2 == 0:
        return find_min_arr(a, b // 2)
    else:
        return a // 2, b

a, b = [int(x) for x in input().split()]
print(*find_min_arr(a, b))
