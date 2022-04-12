

def solve():
    n = int(input())
    for i in range(n):
        sx, sy = [int(x) for x in input().split()]
        dx, dy = [int(x) for x in input().split()]
        t = int(input())
        if (abs(dx - sx) + abs(dy - sy)) == t:
            print("Y")
        else:
            print("N")

solve()
