

def solve(n, wall):
    # Complete this function
    if (len(set(wall)) == 1):
        return "YES"
    else:
        d = max(wall) - min(wall)
        if (d == 1):
            return "YES"
        elif (d == 0):
            return "YES"
        else:
            return "NO"

n = int(input().strip())
wall = list(map(int, input().strip().split(' ')))
print(solve(n, wall))
