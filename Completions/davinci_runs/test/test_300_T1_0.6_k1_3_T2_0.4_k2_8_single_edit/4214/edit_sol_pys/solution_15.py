import math

def dist(x1, y1, x2, y2):
    return math.sqrt( (x1 - x2) ** 2 + (y1 - y2) ** 2 )

def main():
    n = int(input())
    # x_y_list = [tuple(map(int, input().split())) for i in range(n)]
    x_y_list = [tuple(map(int, input().split())) for i in range(n)]

    # n!
    n_factorial = math.factorial(n)


    # All possible paths
        # print(path)
    paths = []
    def inner(path):
        if len(path) == n:
            paths.append(path)
            # print(path)
        else:
            for i in range(n):
                # print(i)
                # print(path)
                if i not in path:
                    # print(path)
                    inner(path + [i])

    inner([])
    # print(paths)

    # All lengths of paths
        # print(path)
    lengths = [0] * n_factorial
            # print(path[j])
            # print(path[j + 1])
            # print(dist(x_y_list[path[j]][0], x_y_list[path[j]][1], x_y_list[path[j + 1]][0], x_y_list[path[j + 1]][1]))
    for i, path in enumerate(paths):
        # print(lengths[i])
        for j in range(n - 1):
    # print(lengths)
            lengths[i] += dist(x_y_list[path[j]][0], x_y_list[path[j]][1], x_y_list[path[j + 1]][0], x_y_list[path[j + 1]][1])

    # Average length
    avg_length = sum(lengths) / n_factorial
    print(avg_length)

if __name__ == '__main__':
    main()
