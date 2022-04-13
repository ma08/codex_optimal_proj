from bisect import bisect_left

def speed_and_distance(stones, distances):
    distance = []
    for i in range(len(stones) - 1):
        distance.append(stones[i + 1] - stones[i])

    if len(set(distance)) == 1:
        print(1, distance[0], sep='\n')
    else:
        print(0, sep='\n')

if __name__ == "__main__":
    M, N = map(int, input().split())
    stones = list(map(int, input().split()))
    distances = list(map(int, input().split()))
    speed_and_distance(stones, distances)
