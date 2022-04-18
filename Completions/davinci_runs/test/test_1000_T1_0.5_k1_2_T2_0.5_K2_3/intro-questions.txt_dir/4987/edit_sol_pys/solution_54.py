
def main():
    socks, color_diff = map(int, input().split())
    machines = 0
    colors = [int(x) for x in input().split()]
    colors.sort()
    i = 0
    while i < socks:
        machines += 1
        j = i + 1
        while j < socks and colors[j] - colors[i] <= color_diff:
            j += 1
        i = j
    print(machines)


if __name__ == "__main__":
    main()
