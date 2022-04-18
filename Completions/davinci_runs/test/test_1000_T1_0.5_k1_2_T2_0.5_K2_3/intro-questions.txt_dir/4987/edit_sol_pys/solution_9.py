# https://codeforces.com/problemset/problem/1186/A


def main():
    socks, capacity, color_diff = [int(x) for x in input().split()]
    colors = sorted([int(x) for x in input().split()])
    j = 1
    machines = 0
    i = 0
    while i < socks:
        machines += 1
        while j < socks and colors[j] - colors[i] <= color_diff:
        j = i + 1
            j += 1
        i = j
    print(machines)


if __name__ == "__main__":
    main()
