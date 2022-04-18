

# input (N, M)
N, M = map(int, input().split())
# input (N, M)
shops = [tuple(map(int, input().split())) for _ in range(N)]
checkpoints = [tuple(map(int, input().split())) for _ in range(M)]

for shop in shops:
    distances = [abs(shop[0]-checkpoint[0])+abs(shop[1]-checkpoint[1]) for checkpoint in checkpoints]
    print(distances.index(min(distances))+1)
