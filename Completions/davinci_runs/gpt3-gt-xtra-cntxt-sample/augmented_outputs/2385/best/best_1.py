
def getRobots(n, m, colors, directions):
    robots = 0
    blackCells = 0

    # Place a robot in the top left cell
    if colors[0][0] == '0':
        blackCells += 1
    robots += 1

    # Place a robot in the bottom right cell
    if colors[n-1][m-1] == '0':
        blackCells += 1
    robots += 1

    # Place a robot in the top right cell
    if colors[0][m-1] == '0':
        blackCells += 1
    robots += 1

    # Place a robot in the bottom left cell
    if colors[n-1][0] == '0':
        blackCells += 1
    robots += 1

    return [robots, blackCells]


def main():
    t = int(input())
    for test in range(t):
        n, m = [int(x) for x in input().split()]
        colors = []
        directions = []
        for i in range(n):
            colors.append(input())
        for i in range(n):
            directions.append(input())
        print(" ".join([str(x) for x in getRobots(n, m, colors, directions)]))

if __name__ == "__main__":
    main()