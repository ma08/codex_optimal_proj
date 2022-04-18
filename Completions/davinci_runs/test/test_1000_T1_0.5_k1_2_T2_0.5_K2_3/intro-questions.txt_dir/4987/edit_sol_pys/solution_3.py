
def main():
    socks, capacity, color_diff = map(int, input().split())
    machines = 0
    colors = [int(x) for x in input().split()]  # list comprehension
    colors.sort()
    i = 0
    while i < socks:  # O(n)
        machines += 1
        j = i + 1
        while j < socks and colors[j] - colors[i] <= color_diff:
            j += 1
        i = j
    print(machines)


if __name__ == "__main__":
    main()
