

import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calc_path_length(path):
    length = 0
    for i in range(len(path) - 1):
        length += dist(path[i][0], path[i][1], path[i + 1][0], path[i + 1][1])
    return length

def calc_average_length(paths):
    length = 0
    for path in paths:
        length += calc_path_length(path)
    return length / len(paths)

def generate_paths(path, xs, ys):
    if len(xs) == 0:
        return [path]
    paths = []
    for i in range(len(xs)):
        new_path = path + [(xs[i], ys[i])]
        new_xs = xs[:i] + xs[i + 1:]
        new_ys = ys[:i] + ys[i + 1:]
        paths += generate_paths(new_path, new_xs, new_ys)
    return paths

def main():
    n = int(input())
    xs = []
    ys = []
    for _ in range(n):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)
    paths = generate_paths([], xs, ys)
    print(calc_average_length(paths))

if __name__ == '__main__':
    main()