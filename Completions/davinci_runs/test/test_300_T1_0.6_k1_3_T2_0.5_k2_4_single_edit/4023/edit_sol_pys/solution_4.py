
def solve(n, wall):
    # Complete this function
    if len(set(wall)) == 1:
        return "YES"
    elif len(set(wall)) == 2:
        a = wall.count(max(wall))
        b = wall.count(min(wall))
        if a == 1 and b == 1:
            return "NO"
        else:
            return "YES"
    else:
        return "NO"

n = int(input().strip())
wall = list(map(int, input().strip().split(' ')))
print(solve(n, wall))
