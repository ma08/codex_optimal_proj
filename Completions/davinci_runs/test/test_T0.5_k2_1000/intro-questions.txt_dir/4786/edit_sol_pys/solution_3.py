
n = int(input())
keywords = [input().lower().replace("-", " ") for _ in range(n)] # replace hyphen with space
similar = set()
for i in range(n):
    for j in range(i+1, n):
        if keywords[i] == keywords[j]:
            similar.add(keywords[i])
print(n - len(similar))
