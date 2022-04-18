def solve(n, m, c, s):
    """Solves the problem"""
    # Place robots in the order described in the problem statement
    robots = [(0,0), (n-1, m-1), (0, m-1), (n-1, 0)]

    # Count the number of robots
    num_robots = 0
    for i, j in robots:
        if i >= 0 and i < n and j >= 0 and j < m:
            num_robots += 1

    # Count the number of black cells
    num_black = 0
    for i, j in robots:
        if i >= 0 and i < n and j >= 0 and j < m:
            if c[i][j] == '0':
                num_black += 1

    return num_robots, num_black

def main():
    """Main"""
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        c = []
        s = []
        for _ in range(n):
            c.append(list(input()))
        for _ in range(n):
            s.append(list(input()))
        print(*solve(n, m, c, s))

main()