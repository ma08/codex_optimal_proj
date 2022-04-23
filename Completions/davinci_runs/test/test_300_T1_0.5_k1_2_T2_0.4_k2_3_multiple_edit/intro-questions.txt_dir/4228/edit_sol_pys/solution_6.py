

N, L = map(int, input().split())

apples = [L + i for i in range(N)]

apples.remove(max(apples, key=abs))

print(sum(apples))
