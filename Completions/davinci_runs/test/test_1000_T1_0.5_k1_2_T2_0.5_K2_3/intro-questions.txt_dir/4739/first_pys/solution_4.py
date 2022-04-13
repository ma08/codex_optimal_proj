

# SOLUTION
import sys

def read_ints():
    return [int(x) for x in sys.stdin.readline().split()]

def solve(m, n, t, x):
    t_min, t_max = t[0], t[-1]
    x_min, x_max = x[0], x[-1]
    x_diff = x_max - x_min
    t_diff = t_max - t_min
    speeds = set()
    for i in range(m-1):
        for j in range(i+1, m):
            speed = (x[j] - x[i]) / (t[j] - t[i])
            speeds.add(speed)
    speeds = sorted(speeds)
    print(len(speeds))
    print(' '.join(map(str, speeds)))

if __name__ == "__main__":
    m, n = read_ints()
    t = read_ints()
    x = read_ints()
    solve(m, n, t, x)