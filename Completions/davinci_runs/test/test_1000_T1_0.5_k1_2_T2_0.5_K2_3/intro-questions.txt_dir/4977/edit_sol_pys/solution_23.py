
def solve():
    sx, sy = [int(x) for x in input().split()]
    dx, dy = [int(x) for x in input().split()]
    t = int(input())
    if (abs(dx - sx) + abs(dy - sy)) <= t and (abs(dx - sx) + abs(dy - sy)) % 2 == t % 2:
        print("Y")
    else:
        print("N")

solve()
