
from bisect import bisect_left

def speed_and_distance(stones, distances):
    distance = []
    for i in range(len(stones) - 1):
        distance.append(stones[i + 1] - stones[i])

    if len(set(distance)) == 1:
        print(1)
        print(distance[0])
    else:
        print(0)

if __name__ == "__main__":
    M, N = map(int, input().split()) # M: Number of stones, N: Number of distances
    stones = list(map(int, input().split())) # stones
    distances = list(map(int, input().split())) # distances
    speed_and_distance(stones, distances)
