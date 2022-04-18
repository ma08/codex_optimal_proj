


def main():
    socks, capacity, color_diff = [int(x) for x in input().split()]  # input socks, capacity, color_diff
    colors = [int(x) for x in input().split()]  # input colors
    colors.sort()
    machines = 0  # counter for machines
    i = 0
    while i < socks:
        machines += 1  # add a machine before checking
        j = i + 1
        while j < socks and colors[j] - colors[i] <= color_diff:  # check if the color is in the range
            j += 1
        i = j  # update i
    print(machines)  # print the result


if __name__ == "__main__":
    main()
