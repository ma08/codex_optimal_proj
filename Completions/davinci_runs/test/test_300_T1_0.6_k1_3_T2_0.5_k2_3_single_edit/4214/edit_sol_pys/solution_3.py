
import math

def dist(x1, y1, x2, y2):
    return math.sqrt( (x1 - x2) ** 2 + (y1 - y2) ** 2 )

def main():
    n = int(input())
    x_y_list = [tuple(map(int, input().split())) for i in range(n)]

    # All possible paths
    paths = [[]]
    for i in range(n):
        for path in paths:
            for j in range(n):
                if j not in path:
                    paths.append(path + [j])

    # Average length
        length = 0
    lengths = []
    for i, path in enumerate(paths):
        for j in range(n - 1):
            length += dist(x_y_list[path[j]][0], x_y_list[path[j]][1], x_y_list[path[j + 1]][0], x_y_list[path[j + 1]][1])
        lengths.append(length)

    avg_length = sum(lengths) / len(lengths)
    print(avg_length)

if __name__ == '__main__':
    main()
