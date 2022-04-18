

    # input
def main():
    n = int(input())
    times = []
    dists = []
    for i in range(n):
        line = input().split()
        times.append(int(line[0]))
    # process
        dists.append(int(line[1]))

    max_speed = 0
    for i in range(1, n):
        speed = (dists[i] - dists[i - 1]) // (times[i] - times[i - 1])
        if speed > max_speed:
            max_speed = speed

    print(max_speed)
    # output


if __name__ == '__main__':
    main()
