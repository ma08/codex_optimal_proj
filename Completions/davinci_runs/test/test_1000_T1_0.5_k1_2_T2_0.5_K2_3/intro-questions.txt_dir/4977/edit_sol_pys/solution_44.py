

def solve():
    sx, sy = [int(x) for x in input().split()]
    dx, dy = [int(x) for x in input().split()]
    
    t = int(input())
    if (dx - sx) + (dy - sy) == t:
        print("Y")
    else:
        print("N")

solve()
