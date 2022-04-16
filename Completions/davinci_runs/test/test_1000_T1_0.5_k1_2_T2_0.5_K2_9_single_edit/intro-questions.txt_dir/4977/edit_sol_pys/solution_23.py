

def solve():
    sx, sy = [int(x) for x in input().split()]
    dx, dy = [int(x) for x in input().split()]
    t = int(input())
    if abs(dx - sx) + abs(dy - sy) <= t and (t - abs(dx - sx) - abs(dy - sy)) % 2 == 0:
        print("Y")
    else:
        print("N")

solve()
