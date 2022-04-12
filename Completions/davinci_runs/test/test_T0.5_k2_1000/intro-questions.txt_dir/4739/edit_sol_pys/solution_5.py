
def speed_and_distance(stones, distances):
    distance = [0]
    for i in range(len(stones) - 1):
        distance.append(stones[i + 1] - stones[i])

    print(distance)

    if len(set(distance)) == 1:
        for i in range(len(distances)):
            if distances[i] % distance[0] == 0:
                print(1)
                print(distances[i] // distance[0])
                break
            else:
                print(0)
    else:
        for i in range(len(distances)):
            print(0)

if __name__ == "__main__":
    n, m = map(int, input().split())
    stones = list(map(int, input().split()))
    distances = list(map(int, input().split()))
    speed_and_distance(stones, distances)
