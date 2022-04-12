

def main():
    n = int(input())
    prev_time, prev_distance = [int(x) for x in input().split()]
    max_v = 0
    for i in range(n):
        time, distance = [int(x) for x in input().split()]
        v = (distance - prev_distance) / (time - prev_time)
        if v > max_v:
            max_v = v
        prev_time = time
        prev_distance = distance
    print(int(max_v))

if __name__ == "__main__":
    main()
