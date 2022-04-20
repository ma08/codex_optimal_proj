

N, M = map(int, input().split())
likes = [0] * M
for _ in range(N):
    K = list(map(int, input().split()))
    for i in K[1:]:
        likes[i-1] += 1
print(likes.count(N))