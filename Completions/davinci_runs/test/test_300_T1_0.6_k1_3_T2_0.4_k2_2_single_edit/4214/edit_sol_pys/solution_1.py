
import math

def dist(x1, y1, x2, y2):
    return math.sqrt( (x1 - x2) ** 2 + (y1 - y2) ** 2 )

def main():
    n = int(input())
    x_y_list = list(map(int, input().split()))

    # n!
    n_factorial = math.factorial(n)

    # All possible paths
    paths = []
    def inner(path):
        if len(path) == n:
            paths.append(path)
        else:
            for i in range(n):
                if i not in path:
                    inner(path + [i])
    inner([])

    # All lengths of paths
        length = 0
    lengths = []
    for i, path in enumerate(paths):
        for j in range(n - 1):
            length += dist(x_y_list[path[j] * 2], x_y_list[path[j] * 2 + 1], x_y_list[path[j + 1] * 2], x_y_list[path[j + 1] * 2 + 1])
        lengths.append(length)

    # Average length
    avg_length = sum(lengths) / n_factorial
    print(avg_length)

if __name__ == '__main__':
    main()
