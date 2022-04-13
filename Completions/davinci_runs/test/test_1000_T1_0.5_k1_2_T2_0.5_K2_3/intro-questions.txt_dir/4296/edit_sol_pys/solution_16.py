def solve(a,b):
    if a == 0:
        return "0"
    elif a == 1:
        if b == 0:
            return "1"
        elif b == 1:
            return "10"
    else:
        if b == 0:
            return "0"
        elif b == 1:
            return "1"

a,b = map(int, input().split())
print(solve(a,b))
