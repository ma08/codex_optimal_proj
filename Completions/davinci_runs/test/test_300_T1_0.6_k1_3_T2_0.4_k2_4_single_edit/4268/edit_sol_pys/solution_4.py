
from sys import stdin

stdin.readline()
points = [tuple(map(int, line.strip().split())) for line in stdin]


def num_pairs_with_integer_distance(points):
    num_pairs = 0
    distances = {}
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            key = tuple(sorted([p1, p2]))  # sort the points so that we can use them as a key
            if key in distances:
                continue
            else:
                distances[key] = sum((x1 - x2) ** 2 for x1, x2 in zip(p1, p2))
            if distances[key] == int(distances[key]):
                num_pairs += 1
    return num_pairs


def main():
    print(num_pairs_with_integer_distance(points))


if __name__ == '__main__':
    main()
