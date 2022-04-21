

def find_min_arr(a, b):
    if a == b:
        return [b]
    return [a, b]

a, b = [int(x) for x in input().split()]
arr = find_min_arr(a, b)
if arr:
    print("YES")
    print(*arr)
else:
    print("NO")
