

N, M = map(int, input().split())
for i in range(10 ** N):
    if all(str(i).zfill(N)[s - 1] == str(c) for s, c in (map(int, input().split()) for _ in range(M))):  # noqa: E501
        print(i)
        exit()
print(-1)
