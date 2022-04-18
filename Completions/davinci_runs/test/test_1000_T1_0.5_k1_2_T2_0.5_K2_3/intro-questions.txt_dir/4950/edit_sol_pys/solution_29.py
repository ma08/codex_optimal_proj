import sys

def main():
    n = int(sys.stdin.readline())
    times = []
    distances = []
    for i in range(n):
        times.append(int(sys.stdin.readline()))
        distances.append(int(sys.stdin.readline()))

    max_speed = 0
    for i in range(n):
        for j in range(i+1, n):
            time_diff = times[j] - times[i]
            dist_diff = distances[j] - distances[i]
            speed = dist_diff / float(time_diff)
            if speed > max_speed:
                max_speed = speed

    print(max_speed)

if __name__ == '__main__':
    main()
