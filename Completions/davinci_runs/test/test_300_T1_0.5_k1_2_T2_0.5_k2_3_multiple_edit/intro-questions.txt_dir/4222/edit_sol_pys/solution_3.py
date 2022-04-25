
N, K = map(int, input().split())

A_list = []
for i in range(K):
    d = int(input())
    A_list.append(list(map(int, input().split())))

A_set = set()
for i in range(K):
    A_set.update(A_list[i])

ans = N - len(A_set)
print(ans)
