

def solve(n, wall):
    # Complete this function    
    return "YES" if (len(set(wall)) <= 2) else "NO"

n = int(input().strip())
wall = list(map(int, input().strip().split(' ')))
print(solve(n, wall))
