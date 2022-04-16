
def main():
    socks, capacity, color_diff = [int(x) for x in input().split()]
    colors = [int(x) for x in input().split()]
    colors.sort()
    machines = 0
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
