
def speed_and_distance(stones, distances):
    if len(set(stones)) == 1:
        print(1)
        print(stones[0])
        return

    if len(set(distance)) == 1:
        speed = []
        distance = []
        for i in range(len(stones) - 1):
            distance.append(stones[i + 1] - stones[i])
            speed.append(distance[i] / distances[i])
        print(len(set(speed)))
        print(*speed)
        return
    else:
        print(0)

if __name__ == "__main__":
    M, N = map(int, input().split())
    stones = list(map(int, input().split()))
    distances = list(map(int, input().split()))
    speed_and_distance(stones, distances)
