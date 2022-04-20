

import sys
import re

def read_input(filename):
    with open(filename, 'r') as f:
        t = int(f.readline())
        cases = []
        for _ in range(t):
            n, m = map(int, f.readline().split())
            tiles = {}
            for _ in range(n):
                tile = []
                for _ in range(2):
                    tile.append(list(map(int, f.readline().split())))
                tiles[str(tile)] = True
            cases.append((n, m, tiles))
        return cases

def solve(case):
    n, m, tiles = case
    if m % 2 == 1:
        return "NO"
    if n == 1:
        return "YES"
    for tile in tiles:
        for t in tiles:
            if t == tile:
                continue
            if str([tile[0][0], tile[1][0], t[0][0], t[1][0]]) in tiles and str([tile[0][1], tile[1][1], t[0][1], t[1][1]]) in tiles:
                return "YES"
    return "NO"

def write_output(filename, solutions):
    with open(filename, 'w') as f:
        for i, sol in enumerate(solutions):
            f.write("Case #%d: %s\n" % (i+1, sol))

def main():
    cases = read_input(sys.argv[1])
    solutions = [solve(case) for case in cases]
    write_output(sys.argv[2], solutions)

if __name__ == "__main__":
    main()