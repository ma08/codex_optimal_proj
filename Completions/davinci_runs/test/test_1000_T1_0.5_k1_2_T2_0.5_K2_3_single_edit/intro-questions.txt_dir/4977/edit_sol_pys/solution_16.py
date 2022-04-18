

def solve():
    sx, sy = map(int, input().split())
    dx, dy = map(int, input().split())
    t = int(input())
    if (dx - sx + dy - sy) == t:
        print("Y")
    else:
        print("N")

solve()
