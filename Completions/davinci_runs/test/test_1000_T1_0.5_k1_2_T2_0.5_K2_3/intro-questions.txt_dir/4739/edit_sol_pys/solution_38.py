
from bisect import bisect_left

def speed_and_distance(stones, distances):
    stones = sorted(stones)
    distances = []
    for i in range(len(stones) - 1):
        distances.append(stones[i + 1] - stones[i])

    if len(set(distances)) == 1:
        print(1)
        print(distances[0])
    else:
        print(0)

if __name__ == "__main__":
    M, N = map(int, input().split())
    stones = list(map(int, input().split()))
    distances = list(map(int, input().split()))
    speed_and_distance(stones, distances)
