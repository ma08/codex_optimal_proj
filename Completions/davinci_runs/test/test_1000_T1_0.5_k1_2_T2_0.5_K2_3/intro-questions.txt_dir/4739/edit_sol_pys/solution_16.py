
from bisect import bisect_left

def speed_and_distance(stones, distances):
    new_distances = []
    for i in range(len(distances) - 1):
        new_distances.append(distances[i + 1] - distances[i])

    if len(set(new_distances)) == 1:
        print(1)
        print(new_distances[0])
    else:
        print(0)

if __name__ == "__main__":
    M, N = map(int, input().split())
    stones = list(map(int, input().split()))
    distances = list(map(int, input().split()))
    speed_and_distance(stones, distances)
