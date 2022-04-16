def speed_and_distance(stones, distances):
    speed, distance = 0, 0
    for i in range(len(stones)-1):
        distance = stones[i+1] - stones[i]
        if distance in distances:
            speed += 1
            distances.remove(distance)
    print(speed)
    print(distance)

if __name__ == "__main__":
    M, N = map(int, input().split())
    stones = list(map(int, input().split()))
    distances = list(map(int, input().split()))
    speed_and_distance(stones, distances)
