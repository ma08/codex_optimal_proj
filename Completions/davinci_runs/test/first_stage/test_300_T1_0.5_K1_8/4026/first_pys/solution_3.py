

def get_input(t):
    inputs = []
    for i in range(t):
        n, m = [int(x) for x in input().split()]
        tiles = []
        for j in range(n):
            t1 = [int(x) for x in input().split()]
            t2 = [int(x) for x in input().split()]
            tiles.append([t1, t2])
        inputs.append([n, m, tiles])
    return inputs

def solve(n, m, tiles):
    if m == 1:
        return True
    if n == 1:
        return False
    if m % 2:
        return False
    if m > 2:
        if m % 4:
            return False
        else:
            return True
    if m == 2:
        for tile in tiles:
            if tile[0][0] == tile[1][1] and tile[0][1] == tile[1][0]:
                return True
        return False

def main():
    t = int(input())
    inputs = get_input(t)
    for n, m, tiles in inputs:
        print("YES" if solve(n, m, tiles) else "NO")

if __name__ == "__main__":
    main()