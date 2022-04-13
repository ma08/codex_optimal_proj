

N, M = map(int, input().split())

file_size = []
for i in range(M):
    file_size.append(int(input()))

file_size.sort(reverse=True)

for i in range(M):
    if N > file_size[i]:
        N -= file_size[i]
        print(i + 1)
        break
