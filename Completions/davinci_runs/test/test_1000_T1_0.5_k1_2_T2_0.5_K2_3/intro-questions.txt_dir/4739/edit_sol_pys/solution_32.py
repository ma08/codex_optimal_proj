
from bisect import bisect_left

def speed_and_time(stones, distances):
    stones_distance = []
    for i in range(len(stones) - 1): # 각 거리를 구해서 리스트에 저장
        stones_distance.append(stones[i + 1] - stones[i])

    if len(set(distance)) == 1:
        print(1)
        print(distance[0])
    else:
        print(0)

if __name__ == "__main__":
    M, N = map(int, input().split())
    stones = list(map(int, input().split()))
    distances = list(map(int, input().split()))
    speed_and_time(stones, distances)
