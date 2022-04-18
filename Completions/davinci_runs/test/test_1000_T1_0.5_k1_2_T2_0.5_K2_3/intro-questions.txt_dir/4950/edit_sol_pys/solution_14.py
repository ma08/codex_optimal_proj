
import sys


def main():
    n = int(sys.stdin.readline())
    times = [0] * n
    distances = [0] * n
    for i in range(n):
        times[i], distances[i] = [int(x) for x in sys.stdin.readline().split()]

    max_speed = 0
    for i in range(n):
        for j in range(i + 1, n):
            time_diff = times[j] - times[i]
            dist_diff = distances[j] - distances[i]
            speed = dist_diff / float(time_diff)
            if speed > max_speed:
                max_speed = speed

    print(max_speed)


if __name__ == '__main__':
    main()
