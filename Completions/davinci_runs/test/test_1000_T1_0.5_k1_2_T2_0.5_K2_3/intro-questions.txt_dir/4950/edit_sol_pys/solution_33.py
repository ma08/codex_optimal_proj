
def main():
    n = int(input())
    prev_time = 0
    prev_dist = 0
    max_speed = 0
    for i in range(n):
        time, dist = [int(x) for x in input().split()] # pylint: disable=C0301
        speed = (dist - prev_dist) / (time - prev_time)
        if speed > max_speed:
            max_speed = speed
        prev_time = time
        prev_dist = dist
    print(int(max_speed))

if __name__ == '__main__':
    main()
