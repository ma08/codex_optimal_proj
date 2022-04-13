

def solve():
    sx, sy = [int(x) for x in input().split()]  # start point
    dx, dy = [int(x) for x in input().split()]  # destination point
    t = int(input())
    if (dx - sx + dy - sy) == t:  # if the distance is equal to the time, it is possible
        print("Y")
    else:
        print("N")


solve()
