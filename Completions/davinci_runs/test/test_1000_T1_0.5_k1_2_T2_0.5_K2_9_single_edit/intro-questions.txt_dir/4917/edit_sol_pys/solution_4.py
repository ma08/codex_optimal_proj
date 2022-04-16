
import sys

def solve(times, n):
    # if any time is within another time, it is impossible
    # otherwise, possible
    for i in range(n):
        for j in range(n):
            if i != j and times[i][0] >= times[j][0] and times[i][1] <= times[j][1]:
                return "gunilla is right"
    return "gunilla has a point"

def main():
    n = int(sys.stdin.readline().strip())
    times = []
    for _ in range(n):
        times.append(tuple(map(int, sys.stdin.readline().strip().split())))
    print(solve(times, n))

if __name__ == "__main__":
    main()
